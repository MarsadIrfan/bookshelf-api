# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
