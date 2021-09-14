from flask import request, Response
from config import app, db
from models import Book

@app.route('/')
def index():
    return "Books API"

@app.route('/books')
def get_all():
    try:
        books = Book.query.all()
        result = []

        for book in books:
            data = { 
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "cover": book.cover
            }
            result.append(data)
        
        return { "books": result }
    except Exception:
        return error_response("There was an error.", 500)

@app.route('/books/<id>')
def get(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return error_response("The ID doesn't exist.", 404)
        return { "id": book.id, "title": book.title, "author": book.author, "cover": book.cover }
    except Exception:
        return error_response("There was an error.", 500)

@app.route('/books', methods=["POST"])
def add():
    try:
        book = Book(title = request.json["title"], author = request.json["author"], cover = request.json["cover"])
        db.session.add(book)
        db.session.commit()

        return { "id": book.id }
    except Exception:
        return error_response("There was an error.", 500)

@app.route('/books/<id>', methods=["DELETE"])
def delete(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return error_response("The ID doesn't exist.", 404)
        db.session.delete(book)
        db.session.commit()

        return Response('', status = 204)
    except Exception:
        return error_response("There was an error deleting the book.", 500)

@app.route('/books/<id>', methods=["PUT"])
def update(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return error_response("The ID doesn't exist.", 404)

        if 'title' in request.json:
            book.title = request.json["title"]
        if 'author' in request.json:
            book.author = request.json["author"]
        if 'cover' in request.json and request.json['cover'] is not None:
            book.cover = request.json["cover"]

        db.session.commit()

        return { "id": book.id, "title": book.title, "author": book.author }
    except Exception:
        return error_response("There was an error updating the book.", 500)

def error_response(message, error_code):
    return Response('{ "error": "' + message + '" }', 
                    status = error_code, 
                    mimetype='application/json')