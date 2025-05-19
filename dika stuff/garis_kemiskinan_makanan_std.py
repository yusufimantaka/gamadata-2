import pandas as pd

# Load the CSV file, skipping the first four rows which contain merged headers
df = pd.read_csv('garis_kemiskinan_makanan_mentah.csv', skiprows=4)

# Define new column names to replace 'Unnamed' and flatten the multi-header structure
columns = ['Provinsi', 
           'Perkotaan_Semester1', 'Perkotaan_Semester2', 'Perkotaan_Tahunan',
           'Perdesaan_Semester1', 'Perdesaan_Semester2', 'Perdesaan_Tahunan',
           'Total_Semester1', 'Total_Semester2', 'Total_Tahunan',
           'Tahun']
df.columns = columns

# Replace '-' with NaN and convert numeric columns to float
df = df.replace('-', pd.NA)
numeric_cols = df.columns[1:-1]  # Exclude 'Provinsi' and 'Tahun'
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Fill missing values with 0 (assuming '-' indicates missing data)
df[numeric_cols] = df[numeric_cols].fillna(0)
df = df.dropna(subset=['Provinsi'])

# Save the processed data to a new CSV file
df.to_csv('Garis Kemiskinan Makanan Cleaned.csv', index=False)

print('Data standardized and saved to Garis Kemiskinan Makanan Cleaned.csv')
