import sqlite3

db = sqlite3.connect(':memory:')



cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(id TEXT, age INTEGER)
''')
db.commit()

cursor.execute('''INSERT INTO users VALUES ('omar', '19') ''')

cursor.execute('''SELECT * FROM users''')
user = cursor.fetchone()
print(user)