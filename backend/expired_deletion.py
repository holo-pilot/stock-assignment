# Code to delete expired products

import sqlite3
from datetime import datetime

# Set current date as variable

current_date = datetime.now().strftime("%Y-%m-%d")

# Open  SQL connection

connection = sqlite3.connect('SQL/stock.db')
cursor = connection.cursor()

# Find and delete from SQL db

cursor.execute("DELETE FROM inventory WHERE expiry = current_date;")

# Commit changes for full delete and close

connection.commit()
connection.close