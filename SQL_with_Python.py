# establishing a connection
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='SQLserver@23')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database Inventory_Management')

# establishing a connection to a specific database
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='SQLserver@23',database='Inventory_management')
cur=mydb.cursor()

# Creating the tables
cur.execute('Create table manufacture (manufacture_id INT PRIMARY KEY NOT NULL, product_name VARCHAR(20), color VARCHAR(20), manufacture_company VARCHAR(20), quantity_required INT, defective_items INT)')
cur.execute('create table goods(goods_id INT NOT NULL, manufacture_id INT FOREIGN KEY NOT NULL, product_name VARCHAR(20), manufacure_date DATE)')
cur.execute('create table purchase(purchase_id INT PRIMARY KEY NOT NULL, goods_id INT, purchase_date DATE, store_name VARCHAR(20), item_name VARCHAR(20), item_quantity INT, purchase_amount INT')
cur.execute('create table sale(sale_id INT PRIMARY KEY NOT NULL, store_name VARCHAR(20), item_name VARCHAR(20), item_quantity INT, profit_margin INT)')


# restablish the connection every time you execute in a new file
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='SQLserver@23',database='Inventory_management')
cur=mydb.cursor()

# Inserting values into manufacture table
m='INSERT INTO manufacture(manufacture_id, product_name, color, manufacture_company, quantity_required, defective_items) VALUES (%s, %s, %s, %s, %s, %s)'
val=[
  (101, 'Wooden chair', 'brown', 'SSExport', 52,2),
  (102, 'Wooden table', 'brown', 'SSExport', 10,3),
  (103, 'Wooden vase', 'brown', 'ABCArts', 20,6),
  (104, 'Red toy car', 'red', 'BioPlastics', 150,8),
  (105, 'Blue toy car', 'blue', 'BioPlastics', 280,7),
  (106, 'Blue barbie bathtub', 'blue', 'BioPlastics', 300,10),
  (107, 'Red surprise toy', 'red', 'WonderToys', 500,9)
  ]
cur.executemany(m,val)
mydb.commit()
print(cur.rowcount, "were inserted.")

# Inserting values into goods table
g='INSERT INTO goods(goods_id, manufacture_id, product_name, manufacture_date) VALUES (%s, %s, %s, %s)'
gval=[
  (111, 101, 'Wooden chair', '2022-10-26'),
  (222, 102, 'Wooden table', '2022-12-26'),
  (333, 103, 'Wooden vase', '2022-10-02'),
  (444, 104, 'Red toy car', '2022-09-13'),
  (555, 105, 'Blue toy car', '2022-08-22'),
  (666, 106, 'Blue barbie bathtub', '2023-02-18'),
  (777, 107, 'Red surprise toy', '2022-10-26')
  ]
cur.executemany(g,gval)
mydb.commit()
print(cur.rowcount, "were inserted.")

# Inserting values into purchase table
p='INSERT INTO purchase(purchase_id, goods_id, purchase_date, store_name, item_name, item_quantity, purchase_amount) VALUES (%s, %s, %s, %s, %s, %s, %s)'
pval=[
    (1234, 111, '2022-12-23','ORay', 'Wooden chair', 8, 5000),
    (1235, 222, '2022-12-23','MyCare', 'Wooden table', 2, 8000),
    (1236, 444, '2022-11-13','MyKids', 'Red toy car', 20, 300),
    (1237, 777, '2022-12-24','MyKids', 'Red surprise toy', 4, 500),
    (1238, 666, '2022-10-23','MyKids', 'Blue barbie bathtub', 3, 800),
    (1239, 333, '2023-01-5','MyCare', 'Wooden vase', 2, 3000)
]
cur.executemany(p,pval)
mydb.commit()
print(cur.rowcount, "were inserted.")

# Inserting values into sale table
s='INSERT INTO sale(sale_id, store_name, item_name, item_quantity, profit_margin) VALUES (%s,%s,%s,%s)'
sval=[
    (6789, 'ORay', 'Wooden chair', 8, 1000),
    (7789, 'MyCare', 'Wooden table', 2, 2000),
    (8789, 'MyKids', 'Red toy car', 20, 100),
    (9789, 'MyKids', 'Red surpise toy', 4, 200),
    (10789, 'MyKids', 'Blue barbie bathtub', 3, 180),
    (11789, 'MyCare', 'Wooden vase', 2, 500) 
]
cur.executemany(s,sval)
mydb.commit()
print(cur.rowcount, "were inserted.")

# restablish the connection every time you execute in a new file
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='SQLserver@23',database='Inventory_management')
cur=mydb.cursor()

# Applying join on the tables
cur.execute('SELECT * FROM manufacture JOIN goods ON manufacture.manufacture_id = goods.manufacture_id JOIN purchase ON goods.goods_id = purchase.goods_id JOIN sale ON purchase.item_quantity = sale.item_quantity')


# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
cur.execute("UPDATE manufacture SET manufacture_company = 'NewManufacturer', quantity_required = 100 WHERE color = 'red' AND manufacture.manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM purchase WHERE store_name = 'MyKids' AND item_name LIKE '%toy car' OR item_name = 'Red surprise toy'))")


# Display all the “wooden chair” items that were manufactured before the 1st May 2023. 
cur.execute("SELECT * FROM manufacture m JOIN goods g ON m.manufacture_id = g.manufacture_id WHERE m.product_name = 'Wooden chair' AND g.manufacure_date < '2023-05-01'")


#  Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
cur.execute("SELECT sale.profit_margin FROM manufacture JOIN goods ON manufacture.manufacture_id = goods.manufacture_id JOIN purchase ON goods.goods_id = purchase.goods_id JOIN sale ON purchase.item_name = sale.item_name WHERE manufacture.product_name = 'Wooden table' AND manufacture.manufacture_company = 'SSExport' AND purchase.store_name='MyCare'")











