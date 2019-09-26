import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

user_query = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY , username text, password text)"
cursor.execute(user_query)

item_query = "CREATE TABLE IF NOT EXISTS Items(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(item_query)

connection.commit()
connection.close()