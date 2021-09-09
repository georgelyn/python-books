from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# db.create_all()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    author = db.Column(db.String(120))
    cover = db.Column(db.String(500))

    def __repr__(self):
        return {f"[{self.id}] - {self.name} by {self.author}"}

@app.route('/')
def index():
    return "Books API"

@app.route('/books')
def get_all():
    books = Book.query.all()
    result = []

    for book in books:
        data = { 
            "id": book.id,
            "name": book.name,
            "author": book.author,
            "cover": book.cover
        }
        result.append(data)
    
    return { "books": result }


@app.route('/books/<id>')
def get(id):
    book = Book.query.get(id)
    if book is None:
        return error_response("The ID doesn't exist.", 404)
    return { "id": book.id, "name": book.name, "author": book.author, "cover": book.cover }
    

@app.route('/books', methods=["POST"])
def add():
    book = Book(name = request.json["name"], author = request.json["author"], cover = request.json["cover"])
    db.session.add(book)
    db.session.commit()

    return { "id": book.id }


@app.route('/books/<id>', methods=["DELETE"])
def delete(id):
    book = Book.query.get(id)
    if book is None:
        return error_response("The ID doesn't exist.", 404)
    db.session.delete(book)
    db.session.commit()

    return Response('', status = 204)


@app.route('/books/<id>', methods=["PUT"])
def update(id):
    book = Book.query.get(id)
    if book is None:
        return error_response("The ID doesn't exist.", 404)

    if 'name' in request.json:
        book.name = request.json["name"]
    if 'author' in request.json:
        book.author = request.json["author"]
    if 'cover' in request.json:
        book.cover = request.json["cover"]

    db.session.commit()

    return { "id": book.id, "name": book.name, "author": book.author }


def error_response(message, error_code):
    return Response('{ "error": ' + message + ' }', 
                    status = error_code, 
                    mimetype='application/json')
