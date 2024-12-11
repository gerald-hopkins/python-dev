import pandas as pd

# Specify the input and output file paths
input_file = '/Users/geraldhopkins/Documents/PythonFiles/Data/Electric_Vehicle_Population_Data.csv'   # Replace with the path to your input CSV file
output_file = '/Users/geraldhopkins/Documents/PythonFiles/Data/Electric_Vehicle_Population_Data_1_1000.csv'  # Replace with the desired output file path

# Read the CSV file and select rows 1001 to 2000
df = pd.read_csv(input_file)

header = df.head(1)

# Select rows 1001 to 2000 (pandas uses 0-based indexing)
df_selected = df.iloc[:1000]

# df_combined = pd.concat([header,df_selected])

# Write the selected rows to the new CSV file
# df_combined.to_csv(output_file, index=False)
df_selected.to_csv(output_file, index=False)

print(f"Rows 2001 through 3000 have been copied to {output_file}")
