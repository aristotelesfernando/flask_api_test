import pymysql
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def db_connection():
    conn = None
    try:          
        conn = pymysql.connect(
            host='sql10.freesqldatabase.com',
            database='sql10616061',
            user='sql10616061',
            password='bV27Ij6MbP',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor            
        )
    except pymysql.error as e:
        print(e)
    return conn

@app.route('/books', methods=['GET','POST'])
def books():

    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute("select * from book")
        books = [
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()            
        ]
        if books is not None:
            return jsonify(books)
        else:
            'Nothing Found', 404
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']

        sql = """INSERT INTO book (author, language, title) VALUES (%s, %s, %s)"""

        cur = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"The new book has sucesseful created"

        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):

    conn = db_connection()
    cursor = conn.cursor()
    boook = None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=%s", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Book with the Id {id} not found", 404

    if request.method == 'PUT': 
        sql = """UPDATE book
            SET title=%s,
                author=%s,
                language=%s
            WHERE id=%s"""
         
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
    
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }

        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)
    
    if request.method == 'DELETE':
        sql = """DELETE FROM book WHERE id=%s"""
        cursor.execute(sql,(id,))
        conn.commit()
        return "The book with the Id: {} has been deleted.".format(id), 200
    
if __name__ == '__main__':
    app.run(debug=True)