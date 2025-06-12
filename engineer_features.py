import pandas as pd

# Load the processed data
processed_file_path = "processed_daily_payments.csv"
df = pd.read_csv(processed_file_path)

# Ensure 'Payment Date' is in datetime format
df['Payment Date'] = pd.to_datetime(df['Payment Date'])

print("Loaded DataFrame head:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Feature Engineering
df['day_of_week'] = df['Payment Date'].dt.dayofweek # Monday=0, Sunday=6
df['day_of_month'] = df['Payment Date'].dt.day
df['month'] = df['Payment Date'].dt.month
df['year'] = df['Payment Date'].dt.year

# Create 'days_since_start' feature
df = df.sort_values(by='Payment Date').reset_index(drop=True) # Ensure it's sorted before creating this
df['days_since_start'] = (df['Payment Date'] - df['Payment Date'].min()).dt.days

print("\nDataFrame head after feature engineering:")
print(df.head())
print("\nDataFrame tail after feature engineering (to see 'days_since_start' progression):")
print(df.tail())

# Save the featured data
featured_file_path = "featured_daily_payments.csv"
df.to_csv(featured_file_path, index=False)
print(f"\nFeatured data saved to {featured_file_path}")

# Display info about the final dataframe
print("\nInfo for final 'featured_daily_payments' DataFrame:")
df.info()
