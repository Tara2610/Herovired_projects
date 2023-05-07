# establishing a connection
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='SQLserver@23',database='Inventory_management')
cur=mydb.cursor()

# Creating the tables
cur.execute
('Create table manufacture (manufacture_id INT PRIMARY KEY NOT NULL, product_name VARCHAR(20), color VARCHAR(20), manufacture_company VARCHAR(20), quantity_required INT, defective_items INT)')
cur.execute
('create table goods(goods_id INT NOT NULL, manufacture_id INT FOREIGN KEY NOT NULL, product_name VARCHAR(20), manufacure_date DATE)')
cur.execute
# ('create table purchase(purchase_id INT PRIMARY KEY NOT NULL, goods_id INT, purchase_date DATE, store_name VARCHAR(20), item_name VARCHAR(20), item_quantity INT, purchase_amount INT')
cur.execute
('create table sale(sale_id INT PRIMARY KEY NOT NULL, store_name VARCHAR(20), item_name VARCHAR(20), item_quantity INT, profit_margin INT)')
