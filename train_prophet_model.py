import pandas as pd
from prophet import Prophet
import json
from prophet.serialize import model_to_json

# Load the featured data
featured_file_path = "featured_daily_payments.csv"
df = pd.read_csv(featured_file_path)

# Ensure 'Payment Date' (which will be 'ds') is in datetime format
df['Payment Date'] = pd.to_datetime(df['Payment Date'])

print("Loaded featured DataFrame head:")
print(df.head())

# Prepare data for Prophet
# Prophet expects columns 'ds' (datestamp) and 'y' (numeric value to forecast)
prophet_df = df[['Payment Date', 'Total Payments Value']].copy()
prophet_df.rename(columns={'Payment Date': 'ds', 'Total Payments Value': 'y'}, inplace=True)

print("\nDataFrame head prepared for Prophet:")
print(prophet_df.head())
print(f"Training data period: {prophet_df['ds'].min()} to {prophet_df['ds'].max()}")
print(f"Number of training data points: {len(prophet_df)}")

# Instantiate and fit the Prophet model
# Default settings include yearly and weekly seasonality.
# Prophet automatically detects trends and changepoints.
# changepoint_prior_scale can be tuned if more flexibility for trend changes is needed.
# For now, we use the default. A higher value makes the trend more flexible.
model = Prophet(changepoint_prior_scale=0.05) # Default is 0.05

# Add monthly seasonality, as payments might have strong monthly patterns (e.g. start/end of month)
# Prophet by default has weekly and yearly.
# Using 10 as Fourier order for monthly seasonality is a common starting point.
model.add_seasonality(name='monthly', period=30.5, fourier_order=10)


# Fit the model to the entire dataset
model.fit(prophet_df)
print("\nProphet model fitting complete.")

# Save the trained model
model_path = "prophet_model.json"
with open(model_path, 'w') as fout:
    json.dump(model_to_json(model), fout)

print(f"Trained Prophet model saved to {model_path}")
