import sqlite3

conn = sqlite3.connect("book.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id integer PRYMARY KEY AUTOINCREMENT,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""

cursor.execute(sql_query)
