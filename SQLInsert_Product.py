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
        cursor.execute('''
        INSERT INTO dbo.product
                (
                product_name,
                product_sku,
                supplier_id,
                date_created
                )
        VALUES 
            ('dog bone','DOG-3389',1,'10/25/2024'),
            ('cat bowl','CAT-8234',3,'10/25/2024'),
            ('fish tank','FSH-3789',5,'10/25/2024'),
            ('fish food','FSH-2139',4,'10/25/2024'),
            ('dog food','DOG-3652',3,'10/25/2024'),
            ('dog leash','DOG-7782',1,'10/25/2024'),
            ('kitty litter','CAT-8732',5,'10/25/2024'),
            ('dog whistle','DOG-8338',2,'10/25/2024'),
            ('cat mouse toy','CAT-2804',1,'10/25/2024'),
            ('dog biscuit','DOG-0398',4,'10/25/2024')
        ;
        ''')



except Exception as e:
    print("Error occurred:", e)

print("All records inserted successfully.")