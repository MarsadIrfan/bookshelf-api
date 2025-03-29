# app.py
from flask import Flask, request
from flask_restful import Api, Resource
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

# Define a Resource for the Book model
class BookResource(Resource):
    def get(self, book_id=None):
        if book_id:
            book = Book.query.get(book_id)
            if book:
                return {"id": book.id, "title": book.title, "author": book.author}, 200
            return {"message": "Book not found"}, 404
        books = Book.query.all()
        return [{"id": book.id, "title": book.title, "author": book.author} for book in books], 200

    def post(self):
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Book created successfully"}, 201

    def put(self, book_id):
        data = request.get_json()
        book = Book.query.get(book_id)
        if book:
            book.title = data['title']
            book.author = data['author']
            db.session.commit()
            return {"message": "Book updated successfully"}, 200
        return {"message": "Book not found"}, 404

    def delete(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return {"message": "Book deleted successfully"}, 200
        return {"message": "Book not found"}, 404

# Add the resource routes
api.add_resource(BookResource, '/books', '/books/<int:book_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
