import os

from flask import Flask, session, render_template, request, redirect, url_for, abort
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text

from passlib.hash import bcrypt

import json

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=['GET', 'POST'])
def index():
    if session.get('id'):
        query = request.args.get('book')
        books = db.execute(text("""SELECT * from "books";""")).fetchall()
        if query is None:
                if request.method == 'GET':
                    return render_template('index.html', books=books, error=False)
                elif request.method == 'POST':
                    session.clear()
                    return redirect(url_for('login'))
        else:
            try:
                book = db.execute(text("""SELECT * from "books" WHERE id=:id"""),{"id":query}).fetchone()
            except:
                return render_template('index.html', books=books, error=True)
            if request.method == 'GET':
                reviews = db.execute(text("""SELECT * from "reviews" WHERE book_id=:book_id"""),{"book_id":query}).fetchall()
                review_submitted = False
                for review in reviews:
                    if review['user_id'] == session['id']:
                        review_submitted = True
                        break
                return render_template('index.html', books=books, error=True) if book is None else render_template('book.html', book=book, reviews=reviews, review_submitted=review_submitted)
            elif request.method == 'POST':
                db.execute(text("""INSERT INTO "reviews" (rating, description, book_id, user_id) VALUES (:rating, :description, :book_id, :user_id)"""),{"rating": request.form['rating'], "description": request.form['description'], "book_id": query, "user_id": session['id']})
                reviews = db.execute(text("""SELECT * from "reviews" WHERE book_id=:book_id"""),{"book_id":query}).fetchall()
                db.commit()
                return render_template('book.html', book=book, reviews=reviews, review_submitted=True)
    else:
        return redirect(url_for('login'))
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if session.get('id'):
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=False)
    elif request.method == 'POST':
        user = db.execute(text("""SELECT * from "users" WHERE username=:username"""),{"username":request.form['username']}).fetchone()
        if user and bcrypt.verify(request.form['password'], user['password']):
            session['id'] = user['id']
            return redirect(url_for('index')) 
        else:
            return render_template('login.html', error=True)
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',error=False)
    elif request.method =='POST':
        user = db.execute(text("""SELECT * from "users" WHERE username=:username"""),{"username":request.form['username']}).fetchone()
        if user:
            return render_template('register.html',error=True) 
        else:
            username = request.form['username']
            password = bcrypt.encrypt(request.form['password'])
            db.execute(text("""INSERT INTO "users" (username, password) VALUES (:username, :password)"""),{"username": username, "password": password})
            db.commit()
            return redirect(url_for('login')) 
@app.route('/api/<isbn>')
def api(isbn):
    if session.get('id'):
        book = db.execute(text("""SELECT * from "books" WHERE isbn=:isbn"""),{"isbn":isbn}).fetchone()
        return abort(404, "Book not found") if book is None else json.dumps(dict(book))
    else:
        return redirect(url_for('login')) 
