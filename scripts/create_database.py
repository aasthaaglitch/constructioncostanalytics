import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/cleaned/construction_projects_cleaned.csv")

# Connect to SQLite database
connection = sqlite3.connect("construction_analytics.db")

# Create SQL table
df.to_sql(
    "construction_projects",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("SQL database created successfully!")
print("Table created: construction_projects")
print(f"Rows loaded: {len(df)}")