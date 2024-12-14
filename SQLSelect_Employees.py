import pandas as pd
import pyodbc

# Database connection parameters
server = 'gerald.database.windows.net,1433'
database = 'customers'
username = 'gerald_admin'
password = 'Saints09!'
driver = '{ODBC Driver 17 for SQL Server}'

# Create a connection string
conn_str = f'Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

print('here')

# Establish a connection to the database
with pyodbc.connect(conn_str) as conn:
    cursor = conn.cursor()

try:
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employees')
        rows = cursor.fetchall()
    for row in rows:
        print(dict(zip([column[0] for column in cursor.description], row)))
except Exception as e:
    print("Error occurred:", e)

print("All records selected successfully.")
