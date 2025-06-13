import pandas as pd
import io
import os

# Define the input CSV file
input_csv_file = "12monthspayments.csv"

# Try to read the CSV.
# It's possible the file still has the ^@ characters or needs specific cleaning.
try:
    # First, try to read it as a normal CSV
    df = pd.read_csv(input_csv_file)
except Exception as e_csv:
    print(f"Standard CSV reading failed: {e_csv}. Attempting to read with more cleaning...")
    try:
        with open(input_csv_file, 'r', encoding='utf-8') as f:
            content = f.read()
        # Remove null characters if they exist, as they caused issues before
        content = content.replace('\x00', '').replace('^@', '')
        # Remove potential warning line if it's still there from original fetch
        lines = content.strip().split('\n')
        if len(lines) > 0 and "Warning:" in lines[-1]: # Check if lines is not empty before accessing lines[-1]
            lines = lines[:-1]
        cleaned_csv_string = "\n".join(lines)
        df = pd.read_csv(io.StringIO(cleaned_csv_string))
    except Exception as e_fallback:
        print(f"Fallback CSV reading also failed: {e_fallback}")
        raise # Re-raise the exception if we can't load the data

print("Original data sample (last 5 rows before potential modification):")
print(df.tail())

# Clean column names (strip spaces) just in case
df.columns = df.columns.str.strip()

# Convert 'Payment Date' to datetime objects
# Adding robust date parsing with multiple format attempts if needed, though M/D/YYYY is expected.
try:
    df['Payment Date'] = pd.to_datetime(df['Payment Date'])
except ValueError:
    print("Standard to_datetime failed. Trying format M/D/YYYY explicitly.")
    try:
        df['Payment Date'] = pd.to_datetime(df['Payment Date'], format='%m/%d/%Y')
    except Exception as e_date:
        print(f"Date conversion failed: {e_date}")
        raise

# Filter out entries from June 2025
# We want data *before* June 1, 2025.
df_modified = df[df['Payment Date'] < pd.to_datetime('2025-06-01')]

print("\nModified data sample (last 5 rows after filtering):")
print(df_modified.tail())

# Verify the last date
if not df_modified.empty:
    last_date_in_modified_data = df_modified['Payment Date'].max()
    print(f"\nLast date in the modified data: {last_date_in_modified_data}")
    if last_date_in_modified_data >= pd.to_datetime('2025-06-01'):
        print("ERROR: Data still contains June 2025 entries or later!")
    else:
        print("Confirmed: June 2025 entries removed. Last date is before June 2025.")
else:
    print("Warning: DataFrame is empty after filtering. Check the date range and data.")


# Save the modified DataFrame back to the CSV, overwriting the original
# Ensure we write it out in a clean CSV format without the index.
df_modified.to_csv(input_csv_file, index=False)

print(f"\nModified data saved back to {input_csv_file}")
