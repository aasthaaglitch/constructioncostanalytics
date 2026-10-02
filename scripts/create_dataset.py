import pandas as pd
import numpy as np
from pathlib import Path

# Make the results reproducible
np.random.seed(42)

# Number of construction projects
n = 120

# Basic project information
project_types = [
    "Residential",
    "Commercial",
    "Industrial",
    "Infrastructure"
]

locations = [
    "Ahmedabad",
    "Gandhinagar",
    "Vadodara",
    "Surat",
    "Mumbai",
    "Pune"
]

contractors = [
    "BuildRight",
    "Shapecraft",
    "UrbanBuild",
    "PrimeConstruct",
    "Apex Infra",
    "Vertex Projects"
]

statuses = [
    "Completed",
    "Ongoing",
    "Delayed"
]

# Create project IDs
project_ids = [f"PRJ-{1001 + i}" for i in range(n)]

# Generate project names
project_names = [
    f"{np.random.choice(project_types)} Project {i + 1}"
    for i in range(n)
]

# Generate project characteristics
project_type = np.random.choice(project_types, n)
location = np.random.choice(locations, n)
contractor = np.random.choice(contractors, n)

area_sqft = np.random.randint(15000, 250000, n)

# Planned budget based approximately on project size
budget_per_sqft = np.random.uniform(1500, 3200, n)
planned_budget = area_sqft * budget_per_sqft

# Create realistic cost overruns/underruns
cost_variance = np.random.normal(0.05, 0.12, n)
actual_cost = planned_budget * (1 + cost_variance)

# Cost components
material_cost = actual_cost * np.random.uniform(0.45, 0.60, n)
labour_cost = actual_cost * np.random.uniform(0.18, 0.30, n)
equipment_cost = actual_cost * np.random.uniform(0.05, 0.12, n)

# Remaining cost = other costs
other_cost = actual_cost - material_cost - labour_cost - equipment_cost

# Project dates
start_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2023-01-01", "2025-12-31"),
        n
    )
)

duration_days = np.random.randint(180, 900, n)
end_dates = start_dates + pd.to_timedelta(duration_days, unit="D")

# Project status
status = np.random.choice(
    statuses,
    n,
    p=[0.55, 0.30, 0.15]
)

# Delay days
delay_days = np.where(
    status == "Delayed",
    np.random.randint(15, 180, n),
    np.random.randint(0, 30, n)
)

# Build the dataset
df = pd.DataFrame({
    "Project_ID": project_ids,
    "Project_Name": project_names,
    "Project_Type": project_type,
    "Location": location,
    "Contractor": contractor,
    "Start_Date": start_dates,
    "End_Date": end_dates,
    "Project_Area_SqFt": area_sqft,
    "Planned_Budget": planned_budget.round(2),
    "Actual_Cost": actual_cost.round(2),
    "Material_Cost": material_cost.round(2),
    "Labour_Cost": labour_cost.round(2),
    "Equipment_Cost": equipment_cost.round(2),
    "Other_Cost": other_cost.round(2),
    "Delay_Days": delay_days,
    "Status": status
})

# Introduce a few realistic data-quality issues
df.loc[5, "Contractor"] = np.nan
df.loc[18, "Location"] = "Ahmedabad "
df.loc[27, "Project_Type"] = "commercial"
df.loc[44, "Contractor"] = "Buildright"
df.loc[73, "Status"] = np.nan

# Save the raw dataset
output_path = Path("data/raw/construction_projects_raw.csv")
df.to_csv(output_path, index=False)

print(f"Dataset created successfully: {output_path}")
print(f"Number of projects: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())