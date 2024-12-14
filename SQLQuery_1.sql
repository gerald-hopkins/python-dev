CREATE TABLE employees (

    employee_id INT IDENTITY NOT NULL PRIMARY KEY,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    email VARCHAR(100),

    phone_number VARCHAR(20),

    hire_date DATE,

    job_title VARCHAR(50),

    salary DECIMAL(10, 2)

);

 INSERT INTO dbo.employees (

    first_name,
    last_name,
    email,
    phone_number,
    hire_date,
    job_title,
    salary
 )

 VALUES (

    'Jerry',
    'Jones',
    'jerry@gmail.com',
    '888-999-3434',
    '8/19/1999',
    'boss',
    250000
 )
 ;


--DROP TABLE dbo.employees
--;

SELECT * FROM dbo.employees
;


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


TRUNCATE TABLE dbo.employees
GO
;


CREATE TABLE dbo.product (
    product_id int IDENTITY NOT NULL PRIMARY KEY
    , product_name VARCHAR(50) NOT NULL
    , product_sku VARCHAR(20) NOT NULL
    , supplier_id INT NOT NULL
    , date_created DATETIME
)
;


INSERT INTO dbo.product
    (
        product_name,
        product_sku,
        supplier_id
    )
VALUES
    ('dog bone','DOG-3389',1),
    ('cat bowl','CAT-8234',3),
    ('fish tank','FSH-3789',5),
    ('fish food','FSH-2139',4),
    ('dog food','DOG-3652',3),
    ('dog leash','DOG-7782',1),
    ('kitty litter','CAT-8732',5),
    ('dog whistle','DOG-8338',2),
    ('cat mouse toy','CAT-2804',1),
    ('dog biscuit','DOG-0398',4)
;


CREATE TABLE dbo.orders
    (
        order_id INT IDENTITY NOT NULL PRIMARY KEY
        , customer_id INT NOT NULL
        , order_date DATETIME NOT NULL
        , order_amount DECIMAL(10,2) NOT NULL
        , payment_method INT NOT NULL
    )
    ;

DROP TABLE dbo.orders;


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


TRUNCATE TABLE dbo.product
;

TRUNCATE TABLE dbo.orders
;
