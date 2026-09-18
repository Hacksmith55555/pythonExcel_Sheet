import pandas as pd

# Read the entire Excel file into a DataFrame
df = pd.read_excel('C:/Users/purep/OneDrive/Documents/pythonExcel_Sheet.xlsx', sheet_name='python_Excel')

# View the first 5 rows of data
print(df)
