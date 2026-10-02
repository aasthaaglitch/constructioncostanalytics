import pandas as pd

df = pd.read_csv("data/raw/construction_projects_raw.csv")

print("DATASET SHAPE")
print(df.shape)

print("\nDATASET INFORMATION")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nPROJECT TYPES")
print(df["Project_Type"].unique())

print("\nLOCATIONS")
print(df["Location"].unique())

print("\nCONTRACTORS")
print(df["Contractor"].unique())

print("\nSTATUSES")
print(df["Status"].unique())