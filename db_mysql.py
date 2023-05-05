import pymysql

conn = pymysql.connect(
    host='sql10.freesqldatabase.com',
    database='sql10616061',
    user='sql10616061',
    password='bV27Ij6MbP',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id int AUTO_INCREMENT PRIMARY KEY,
    author varchar(255) NOT NULL,
    language varchar(255) NOT NULL,
    title varchar(255) NOT NULL)"""

cursor.execute(sql_query)
conn.close()
