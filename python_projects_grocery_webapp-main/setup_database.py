import mysql.connector

# Connect to MySQL server (without specifying database)
connection = mysql.connector.connect(user='root', password='123456')
cursor = connection.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS grocery_store")
cursor.execute("USE grocery_store")

# Create uom table
cursor.execute("""
CREATE TABLE IF NOT EXISTS uom (
    uom_id INT AUTO_INCREMENT PRIMARY KEY,
    uom_name VARCHAR(50) NOT NULL
)
""")

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    uom_id INT,
    price_per_unit DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    datetime DATETIME NOT NULL
)
""")

# Create order_details table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_details (
    order_id INT,
    product_id INT,
    quantity DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

# Insert sample UOM data
cursor.execute("INSERT IGNORE INTO uom (uom_name) VALUES ('Kilogram')")
cursor.execute("INSERT IGNORE INTO uom (uom_name) VALUES ('Liter')")
cursor.execute("INSERT IGNORE INTO uom (uom_name) VALUES ('Piece')")
cursor.execute("INSERT IGNORE INTO uom (uom_name) VALUES ('Gram')")

# Insert sample products
cursor.execute("INSERT IGNORE INTO products (name, uom_id, price_per_unit) VALUES ('Rice', 1, 50.00)")
cursor.execute("INSERT IGNORE INTO products (name, uom_id, price_per_unit) VALUES ('Milk', 2, 60.00)")
cursor.execute("INSERT IGNORE INTO products (name, uom_id, price_per_unit) VALUES ('Bread', 3, 40.00)")
cursor.execute("INSERT IGNORE INTO products (name, uom_id, price_per_unit) VALUES ('Sugar', 4, 45.00)")

connection.commit()
print("Database 'grocery_store' created successfully with tables and sample data!")
cursor.close()
connection.close()
