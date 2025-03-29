# test_api.py
import unittest
import json
from app import app, db, Book

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_book(self):
        response = self.app.post('/books', data=json.dumps({
            'title': 'New Book',
            'author': 'Test Author'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
