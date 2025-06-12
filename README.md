
# Payment Receipts Forecasting

## Overview
This project provides a Python script () to forecast daily payment receipts for the next 30 days. It uses 12 months of historical payment data and the Prophet forecasting library.

The script performs the following steps:
1.  Loads payment data from a CSV file.
2.  Cleans and preprocesses the data (handles currency formatting, aggregates daily totals).
3.  Performs feature engineering (extracts time-based features).
4.  Trains a Prophet forecasting model.
5.  Generates a 30-day forecast.
6.  Saves the forecast to .

## Prerequisites
*   Python 3.x
*   pip (Python package installer)

## Installation

1.  **Clone the repository or download the files.**

2.  **Install required Python libraries:**
    Open your terminal or command prompt and run:
    Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pandas in /home/jules/.local/lib/python3.10/site-packages (2.3.0)
Requirement already satisfied: prophet in /home/jules/.local/lib/python3.10/site-packages (1.1.7)
Requirement already satisfied: numpy>=1.22.4 in /home/jules/.local/lib/python3.10/site-packages (from pandas) (2.2.6)
Requirement already satisfied: python-dateutil>=2.8.2 in /home/jules/.local/lib/python3.10/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /home/jules/.local/lib/python3.10/site-packages (from pandas) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /home/jules/.local/lib/python3.10/site-packages (from pandas) (2025.2)
Requirement already satisfied: cmdstanpy>=1.0.4 in /home/jules/.local/lib/python3.10/site-packages (from prophet) (1.2.5)
Requirement already satisfied: matplotlib>=2.0.0 in /home/jules/.local/lib/python3.10/site-packages (from prophet) (3.10.3)
Requirement already satisfied: holidays<1,>=0.25 in /home/jules/.local/lib/python3.10/site-packages (from prophet) (0.74)
Requirement already satisfied: tqdm>=4.36.1 in /home/jules/.local/lib/python3.10/site-packages (from prophet) (4.67.1)
Requirement already satisfied: importlib_resources in /home/jules/.local/lib/python3.10/site-packages (from prophet) (6.5.2)
Requirement already satisfied: stanio<2.0.0,>=0.4.0 in /home/jules/.local/lib/python3.10/site-packages (from cmdstanpy>=1.0.4->prophet) (0.5.1)
Requirement already satisfied: contourpy>=1.0.1 in /home/jules/.local/lib/python3.10/site-packages (from matplotlib>=2.0.0->prophet) (1.3.2)
Requirement already satisfied: cycler>=0.10 in /home/jules/.local/lib/python3.10/site-packages (from matplotlib>=2.0.0->prophet) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /home/jules/.local/lib/python3.10/site-packages (from matplotlib>=2.0.0->prophet) (4.58.2)
Requirement already satisfied: kiwisolver>=1.3.1 in /home/jules/.local/lib/python3.10/site-packages (from matplotlib>=2.0.0->prophet) (1.4.8)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=2.0.0->prophet) (25.0)
Requirement already satisfied: pillow>=8 in /home/jules/.local/lib/python3.10/site-packages (from matplotlib>=2.0.0->prophet) (11.2.1)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/lib/python3/dist-packages (from matplotlib>=2.0.0->prophet) (3.1.1)
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)

    *Troubleshooting Prophet Installation:*
    Prophet can sometimes have complex dependencies. If you encounter issues, please refer to the official Prophet installation guide: [https://facebook.github.io/prophet/docs/installation.html](https://facebook.github.io/prophet/docs/installation.html)

## Data File

*   The script expects an input CSV file containing historical payment data.
*   By default, it looks for a file named  in the same directory as the  script.
*   **Required CSV Columns**:
    1.  : Date of payment (e.g., M/D/YYYY or YYYY-MM-DD).
    2.  : Binary indicator (1 for recurring/autopay, 0 for non-recurring).
    3.  : The monetary value of payments for that record (e.g., " ,234.56 " or 1234.56).

*   **Updating Input Data**:
    To use your own updated data, replace the  file with your new data, ensuring it has the correct columns and format.

*   **Changing Input File Path (Optional)**:
    If your data file has a different name or is in a different location, you can change its path directly in the  script by modifying the  variable at the top of the script:


## Running the Forecast

1.  Ensure your input CSV data (e.g., ) is in the correct location.
2.  Open your terminal or command prompt, navigate to the directory containing .
3.  Execute the script:


## Output

*   **Main Forecast File**:
    This file contains the daily forecasted payment values for the next 30 days, along with lower and upper uncertainty bounds.

*   **Intermediate Files (Optional)**:
    The script also generates the following files by default, which can be useful for inspection or debugging:
    *   : Data after cleaning and daily aggregation.
    *   : Data with engineered features.
    *   : The trained Prophet model.

    You can disable the creation of these intermediate files by setting  near the top of the  script.
