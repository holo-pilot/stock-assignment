import sqlite3

# Define connection and cursor

connection = sqlite3.connect('stock.db')

cursor = connection.cursor()

# Create table

command1 = '''CREATE TABLE IF NOT EXISTS inventory(
   stock_id INT PRIMARY KEY NOT NULL,
   product TEXT NOT NULL,
   amount INT NOT NULL,
   expiry TEXT NOT NULL
); '''


cursor.execute(command1)


# Adding values

cursor.execute("INSERT INTO inventory VALUES ( 1, 'tea', 20, '2025-05-05')")

cursor.execute("INSERT INTO inventory VALUES ( 2, 'coffee', 40, '2025-06-06')")

cursor.execute("INSERT INTO inventory VALUES ( 3, 'coke', 35, '2025-06-07')")

cursor.execute("INSERT INTO inventory VALUES ( 4,'pepsi', 69, '2025-06-06')")


# Commit the changes to the database to for it to show in the viewer

connection.commit() 

# Data check

# cursor.execute("SELECT * FROM inventory;")
# results = cursor.fetchall()
# print(results)

# Close the connection between python and SQLite

connection.close()
