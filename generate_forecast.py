import pandas as pd
from prophet import Prophet
import json
from prophet.serialize import model_from_json

# Load the trained model
model_path = "prophet_model.json"
with open(model_path, 'r') as fin:
    model = model_from_json(json.load(fin))
print(f"Trained Prophet model loaded from {model_path}")

# Load the featured data to get the last date
featured_file_path = "featured_daily_payments.csv"
df = pd.read_csv(featured_file_path)
df['Payment Date'] = pd.to_datetime(df['Payment Date'])
last_date = df['Payment Date'].max()
print(f"Last date in the training data: {last_date}")

# Create a future DataFrame for the next 30 days
# The forecast period starts the day after the last date in the training data
future_df = model.make_future_dataframe(periods=30, freq='D')

print("\nFuture DataFrame tail (should include 30 days past last_date):")
print(future_df.tail())

# Make predictions
forecast_df = model.predict(future_df)

print("\nForecast DataFrame head (raw output from predict):")
print(forecast_df.head())
print("\nForecast DataFrame columns:")
print(forecast_df.columns)

# Select relevant columns for the output
# We are interested in the forecast for the 30 future days only
# The forecast_df contains historical data fit as well, so we slice it
forecast_output_df = forecast_df[forecast_df['ds'] > last_date][['ds', 'yhat', 'yhat_lower', 'yhat_upper', 'trend', 'monthly', 'weekly']].copy()
forecast_output_df.rename(columns={
    'ds': 'Payment Date',
    'yhat': 'Forecasted Total Payments Value',
    'yhat_lower': 'Forecasted Lower Bound',
    'yhat_upper': 'Forecasted Upper Bound'
}, inplace=True)

print("\nForecasted values for the next 30 days (head):")
print(forecast_output_df.head())
print("\nForecasted values for the next 30 days (tail):")
print(forecast_output_df.tail())
print(f"Number of forecasted days: {len(forecast_output_df)}")


# Save the forecast
forecast_file_path = "forecasted_receipts_next_30_days.csv"
forecast_output_df.to_csv(forecast_file_path, index=False)
print(f"\n30-day forecast saved to {forecast_file_path}")

# Optional: Plot the forecast (cannot be done in subtask directly to view, but good for script completeness)
# try:
#     fig1 = model.plot(forecast_df)
#     # fig1.savefig("forecast_plot.png") # Would require matplotlib.pyplot
#     fig2 = model.plot_components(forecast_df)
#     # fig2.savefig("forecast_components_plot.png")
#     print("\n(Forecast plots would be generated here if matplotlib was used and saving enabled)")
# except Exception as e:
#     print(f"Could not generate plots: {e}")
