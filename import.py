import os

import csv

import requests

from sqlalchemy import create_engine
from sqlalchemy.sql import text

#setting up database
engine = create_engine(os.getenv("DATABASE_URL"))
#creating books table
engine.execute(text("""CREATE TABLE "books" (id SERIAL PRIMARY KEY, isbn VARCHAR, TITLE VARCHAR, author VARCHAR, year INTEGER, reviews_count INTEGER, average_rating VARCHAR)"""))
#creating users table
engine.execute(text("""CREATE TABLE "users" (id SERIAL PRIMARY KEY, username VARCHAR, password VARCHAR)"""))
#creating reviews table
engine.execute(text("""CREATE TABLE "reviews" (id SERIAL PRIMARY KEY, rating INTEGER, description VARCHAR, book_id INTEGER REFERENCES books(id), user_id INTEGER REFERENCES users(id))"""))
#inserting values into the books table
with open('books.csv', newline='') as f:
    #next line is to ignore the first line which has the headlines
    next(f)
    data = csv.reader(f, delimiter=",")
    for isbn, title, author, year in data:
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "VuWhJYlE9nkFC2A1e62yg", "isbns": isbn})
        reviews_count = None if res.status_code == 404 else res.json()['books'][0]['reviews_count']
        average_rating = None if res.status_code == 404 else res.json()['books'][0]['average_rating']
        engine.execute(text("""INSERT INTO "books" (isbn, title, author, year, reviews_count, average_rating) VALUES (:isbn, :title, :author, :year, :reviews_count, :average_rating)"""),{"isbn": isbn, "title": title, "author": author, "year": year, "reviews_count": reviews_count, "average_rating": average_rating})
