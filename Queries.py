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

