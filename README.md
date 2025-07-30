# 📚 BookShelf API

Welcome to **BookShelf API** — A clean, RESTful backend service built with **Flask** and powered by a **SQLAlchemy** database. Designed for developers who crave simplicity, scalability, and elegance in their CRUD applications. 🚀

---

## ✨ Features

- 🛠️ **RESTful API** — Built with Flask for a clean and simple interface
- 🧠 **Flask_SQLAlchemy** — ORM magic with zero boilerplate
- 🔄 **Flask_resful** — To define the Resource for the book model 
- 🔬 **Unittest** — Fully tested endpoints to ensure reliability
- 📘 **CRUD for Books** — Create, Read, Update, and Delete your favorite books

---

## 📦 Technologies Used

| Tech Stack | Description |
|------------|-------------|
| 🐍 Flask   | Python micro web framework |
| 📄 Flask_SQLAlchemy | ORM for database management |
| 🔁 Flask_CORS | Handles cross-origin requests |
| 🧪 Unittest | Python’s built-in testing framework |

---

## 📚 API Endpoints

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/books/<id>`    | Get a book by ID       |
| POST   | `/books`         | Add a new book         |
| PUT    | `/books/<id>`    | Update book by ID      |
| DELETE | `/books/<id>`    | Delete book by ID      |

> All responses are in JSON format and follow RESTful conventions.

---

## 🧰 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MarsadIrfan/bookshelf-api.git
cd bookshelf-api
```

### 2. Install dependencies

```bash
pip install flask flask-sqlalchemy flask-restful
```

### 3. Run server and test

```bash
flask run
```

```bash
python apiTest.py
```

### Note: By following these instructions you are installing the packages in python's global environment.

---

### 🧠 Why this project?
This project is ideal for:

- Practicing RESTful API design
- Learning Flask and SQLAlchemy integration
- Building backend skills with Python
- Unit testing for real-world APIs

---

### 🌐 License
This project is open-source under the MIT License. Feel free to fork and expand it!

---

#### 🚀 Contributing
Pull requests are welcome! If you spot an issue or want to improve this project, open an issue or submit a PR. Let’s build something great together. 💪

---
