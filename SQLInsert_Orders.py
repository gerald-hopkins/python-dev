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
        INSERT INTO dbo.orders
                (
                customer_id,
                order_date,
                order_amount,
                payment_method
                )
        VALUES 
            (1,'10/22/2024',250.00,1),
            (2,'10/23/2024',134.95,1),
            (3,'10/23/2024',100.00,2),
            (4,'10/24/2024',59.22,2),
            (1,'10/25/2024',300.00,1),
            (1,'10/25/2024',150.00,1),
            (3,'10/26/2024',99.99,2),
            (6,'10/26/2024',25.00,2),
            (8,'10/26/2024',25.00,1),
            (6,'10/27/2024',75.00,1)
        ;
        ''')



except Exception as e:
    print("Error occurred:", e)

print("All records inserted successfully.")