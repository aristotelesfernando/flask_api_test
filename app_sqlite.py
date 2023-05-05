import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def db_connection():
    conn = None
    try:          
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/books', methods=['GET','POST'])
def books():

    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor = conn.execute("select * from book")
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
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

        sql = """INSERT INTO book (author, language, title) VALUES (?, ?, ?)"""

        cur = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the ID {cur.lastrowid} has sucesseful created"

        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):

    conn = db_connection()
    cursor = conn.cursor()
    boook = None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Book with the Id {id} not found", 404

    if request.method == 'PUT': 
        sql = """UPDATE book
            SET title=?,
                author=?,
                language=?
            WHERE id=?"""
         
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
    
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }

        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)
    
    if request.method == 'DELETE':
        sql = """DELETE FROM book WHERE id=?"""
        conn.execute(sql,(id,))
        conn.commit()
        return "The book with the Id: {} has been deleted.".format(id), 200
    
if __name__ == '__main__':
    app.run(debug=True)