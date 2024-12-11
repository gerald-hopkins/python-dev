import pandas as pd

# Define the source and destination file paths
source_file = '/Users/geraldhopkins/Documents/PythonFiles/Data/Electric_Vehicle_Population_Data.csv'  # Replace with the actual path
destination_file = '/Users/geraldhopkins/Documents/PythonFiles/Data/Electric_Vehicle_Population_Data_test.csv'  # Replace with the desired path

# Read the first 1000 rows from the source CSV file
df = pd.read_csv(source_file, nrows=1000)

# Write the first 1000 rows to the destination CSV file
df.to_csv(destination_file, index=False)

print("First 1000 rows copied successfully.")
