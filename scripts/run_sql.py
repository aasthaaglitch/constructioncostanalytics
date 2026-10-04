import sqlite3
import pandas as pd

# Connect to the SQLite database
connection = sqlite3.connect("construction_analytics.db")

# Read the SQL query from the SQL file
with open("sql/01basicanalysis.sql", "r") as file:
    query = file.read()

# Execute the SQL query
result = pd.read_sql_query(query, connection)

# Display the result
print(result.to_string(index=False))

# Close the connection
connection.close()