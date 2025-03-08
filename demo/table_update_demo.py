# Update section for demo purposes (MUST DELETE)

import sqlite3
from datetime import datetime

connection = sqlite3.connect('SQL/stock.db')
cursor = connection.cursor()

current_date = datetime.now().strftime("%Y-%m-%d")

print(current_date)



cursor.execute('''UPDATE inventory
SET expiry = current_date
WHERE stock_id = 1;''')

connection.commit()
connection.close()
