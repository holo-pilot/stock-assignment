import sqlite3
from datetime import datetime


# Fetch today's date and set as variable

current_date = datetime.now().strftime("%Y-%m-%d")

# Query SQL db for match

connection = sqlite3.connect('SQL/stock.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM inventory WHERE expiry = current_date;")

# print results

date_match = cursor.fetchall()
print(date_match)
connection.close