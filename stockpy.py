import sqlite3

# Define connection and cursor

connection = sqlite3.connect('stock.db')

cursor = connection.cursor()

# Create table

command1 = """CREATE TABLE IF NOT EXISTS inventory(
   stock_id INT PRIMARY KEY NOT NULL,
   product TEXT,
   amount INT,
   expiry TEXT
); """

cursor.execute(command1)
