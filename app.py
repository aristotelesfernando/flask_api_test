import sqlite3
from flask import Flask, request, jsonify

app_sqlite = Flask(__name__)
      

books_list = [
  {
    "id": 1,
    "author": "Mckinney Hughes",
    "language": "Portuguese",
    "title": "ISOSURE"
  },
  {
    "id": 2,
    "author": "Delaney Williamson",
    "language": "Spanish",
    "title": "ZYTRAX"
  },
  {
    "id": 3,
    "author": "Lolita Rich",
    "language": "Germany",
    "title": "KANGLE"
  },
  {
    "id": 4,
    "author": "Dominguez Jenkins",
    "language": "Spanish",
    "title": "ZOLAR"
  },
  {
    "id": 5,
    "author": "Baker Mccoy",
    "language": "Spanish",
    "title": "OVERPLEX"
  },
  {
    "id": 6,
    "author": "Jimmie Ruiz",
    "language": "Spanish",
    "title": "OPTYK"
  }
]

@app.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Founs', 404
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }

        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
            for book in books_list:
                 if book['id'] == id:
                      return jsonify(book)
                 pass
    if request.method == 'PUT': 
         for book in books_list:
              if book['id'] == id:
                   book['author'] = request.form['author']
                   book['language'] = request.form['language']
                   book['title'] = request.form['title']
                   updated_book = {
                        'id': id,
                        'author': book['author'],
                        'language': book['language'],
                        'title': book['title']
                   }
                   return jsonify(updated_book)
    
    if request.method == 'DELETE':
         for index, book in enumerate(books_list):
              if book['id'] == id:  
                   books_list.pop(index)
                   return jsonify(books_list)
    
if __name__ == '__main__':
    app_sqlite.run(debug=True)