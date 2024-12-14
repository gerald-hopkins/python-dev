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
        INSERT INTO dbo.employees
                (
                first_name,
                last_name,
                email,
                phone_number,
                hire_date,
                job_title,
                salary
                )
        VALUES 
            ('Harold','Catchot', 'bigh@yahoo.com', '601-324-6589', '4/1/2003', 'jammer', 345000),
            ('Butch','Henley', 'deez@nutz.com', '223-324-6589', '5/5/2003', 'hornblower', 100000),
            ('Nancy','Drew', 'nd@hotmail.com', '444-324-2310', '7/1/1998', 'teller', 205000),
            ('Dawn','Gibson', 'dawn@yahoo.com', '223-987-6589', '1/5/1984', 'counter', 200000),
            ('Hank','Pym', 'smallest@avengers.com', '888-455-6589', '6/17/2000', 'head cheese', 110000),
            ('Tom','Linkletter', 'toml@brinks.com', '555-222-4433', '4/1/2003', 'fisherman', 50000),
            ('Steve','Rogers', 'cap@yahoo.com', '601-324-6589', '9/1/1932', 'lineman', 500000),
            ('Peggy','Soo', 'oneder@why.com', '212-455-0909', '11/12/2009', 'cowboy', 275000),
            ('Alice','Miner', 'marmin@patriot.com', '228-504-7765', '4/1/1976', 'manager', 89000),
            ('Richard','Patton', 'peggy@ping.com', '601-324-6589', '4/15/2012', 'scrub', 280000)
        ;
        ''')



except Exception as e:
    print("Error occurred:", e)

print("All records inserted successfully.")