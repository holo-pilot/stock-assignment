import sqlite3

# Define connection and cursor

connection = sqlite3.connect('stock.db')

cursor = connection.cursor()

# Create table

command1 = """CREATE TABLE IF NOT EXISTS inventory(
   stock_id INT PRIMARY KEY NOT NULL,
   product TEXT NOT NULL,
   amount INT NOT NULL,
   expiry TEXT NOT NULL
); """


cursor.execute(command1)


# Adding values

cursor.execute("INSERT INTO inventory VALUES ( 1, 'tea', 20, 2025-05-10)")

cursor.execute("INSERT INTO inventory VALUES ( 2, 'coffee', 40, 2025-05-10)")

cursor.execute("INSERT INTO inventory VALUES ( 3, 'coke', 35, 2025-05-10)")

cursor.execute("INSERT INTO inventory VALUES ( 4,'pepsi', 69, 2025-05-10)")

# Data check

# cursor.execute("SELECT * FROM inventory;")
# results = cursor.fetchall()
# print(results)

