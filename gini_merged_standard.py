import pandas as pd

# Define new column names
columns = [
    'Province',
    'Urban_Semester1', 'Urban_Semester2', 'Urban_Annual',
    'Rural_Semester1', 'Rural_Semester2', 'Rural_Annual',
    'UrbanRural_Semester1', 'UrbanRural_Semester2', 'UrbanRural_Annual',
    'Year'
]

# Read CSV with skipped rows
df = pd.read_csv('gini_ratio_merged.csv', skiprows=4, header=None)

# Assign new column names
df.columns = columns

# Replace '-' with NaN and convert numeric columns
df.replace('-', pd.NA, inplace=True)
df.iloc[:, 1:-1] = df.iloc[:, 1:-1].apply(pd.to_numeric, errors='coerce')

# Save cleaned data with 'out_' prefix to comply with sandbox rules
df.to_csv('out_standardized_gini_data.csv', index=False)