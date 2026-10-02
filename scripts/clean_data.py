import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/construction_projects_raw.csv")

print("Before cleaning:")
print(df.isnull().sum())

# Remove extra spaces from text columns
text_columns = [
    "Project_Name",
    "Project_Type",
    "Location",
    "Contractor",
    "Status"
]

for column in text_columns:
    df[column] = df[column].str.strip()

# Standardize capitalization
df["Project_Type"] = df["Project_Type"].str.title()
df["Location"] = df["Location"].str.title()
df["Contractor"] = df["Contractor"].str.title()
df["Status"] = df["Status"].str.title()

# Fill missing categorical values
df["Contractor"] = df["Contractor"].fillna("Unknown")
df["Status"] = df["Status"].fillna("Unknown")

# Save cleaned dataset
output_path = "data/cleaned/construction_projects_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nAfter cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset saved to:")
print(output_path)