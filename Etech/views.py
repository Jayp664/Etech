import sqlite3

db = sqlite3.connect('Database.sqlite3') 
cur = db.cursor()
res= cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(res.fetchall())

res= cur.execute("SELECT total(price) FROM customer_product")
print(res.fetchall())
