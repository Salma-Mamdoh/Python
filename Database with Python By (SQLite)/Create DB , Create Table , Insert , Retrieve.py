# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username, Password)
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# - SQL Stand For Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types (Text, Integer, Date)
# ------------------------------------------------------
# Create Database and connnect

import sqlite3

# Create and connect
db=sqlite3.connect("app.db")
""""
# Create the Table and fields
db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER , user_id INTEGER)")
# Close Database
db.close()
"""


# Insert into Database

# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes

# Setting Up cr
cr=db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER , user_id INTEGER)")
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER,name TEXT)")

cr.execute("INSERT INTO users(user_id , name) values (1,'Salma')")
cr.execute("INSERT INTO users(user_id , name) values (2,'Ahmed')")

db.commit()

mylist=['Mohammed','Sara','Rahma']
for id,user in enumerate(mylist):
    cr.execute(f"INSERT INTO users(user_id , name) values ({id+3},'{user}')")

db.commit()

#Retrieve Data From Database
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>

cr.execute("SELECT name FROM users")
print(cr.fetchone()) # ('Salma',)
print(cr.fetchall()) # [('Ahmed',), ('Mohammed',), ('Sara',), ('Rahma',)]
print(cr.fetchmany(2)) # [('Salma',), ('Ahmed',)]

db.close()







