import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned/construction_projects_cleaned.csv")

print("DATASET SHAPE")
print(df.shape)

print("\nDUPLICATE PROJECT IDs")
print(df["Project_ID"].duplicated().sum())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nNUMERIC SUMMARY")
print(df.describe())

print("\nNEGATIVE VALUES CHECK")

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()
    print(f"{column}: {negative_count} negative values")

print("\nDATE CHECK")

df["Start_Date"] = pd.to_datetime(df["Start_Date"])
df["End_Date"] = pd.to_datetime(df["End_Date"])

invalid_dates = (df["End_Date"] < df["Start_Date"]).sum()

print(f"Projects with End Date before Start Date: {invalid_dates}")