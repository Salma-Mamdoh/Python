# Update
import sqlite3
db=sqlite3.connect("app.db")
cr=db.cursor()
cr.execute("UPDATE users SET name = 'Roaa' ")
cr.execute("SELECT * FROM users")
print(cr.fetchone()) # (1, 'Roaa')
print(cr.fetchone()) # (2, 'Roaa')
print(cr.fetchone()) # (3, 'Roaa')

cr.execute("UPDATE users SET name = 'Omnia' WHERE user_id=1")
cr.execute("SELECT * FROM users")
print(cr.fetchone()) # (1, 'Roaa') # (1, 'Omnia')
print(cr.fetchone()) # (2, 'Roaa') # (2, 'Roaa')
print(cr.fetchone()) # (3, 'Roaa') # (3, 'Roaa')


# Delete
#cr.execute("DELETE FROM users") # will delete all data in users table
cr.execute("DELETE FROM users WHERE name='Omnia'")
cr.execute("SELECT * FROM users")
print(cr.fetchone()) # (2, 'Roaa')
print(cr.fetchone()) # (3, 'Roaa')


