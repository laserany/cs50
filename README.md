# Project 2

Web Programming with Python and JavaScript

This project includes 5 html files (5 pages), static css and javascript files for my login/register pages and 2 python files (one used to initialize my tables and the 2nd one is my application file).

static/index.css and static/index.js: These are mainly used to style my login and register pages and added to my layout.html.

layout.html: my layout file for my login and register pages and it is the file that imports the styles from my index.css and index.js.

login.html: my login page which shows an error on the top if username/password already exists. Has a username and password and has a (create new account) button that redirects to the register page.

register.html: similar to login.html as it allows you to create a new username (if it didn't exist) otherwise will show an error message.

index.html: the main application page that allows you to search for a book and shows an error if the book doesn't exist. Also has a logout button that would log you out (by clearing the session).

book.html: this page will show you the general information abou the book including the reviews. If the user didn't add a review, it will show you an option to pick a rating from 1 to 5 and type a description for that review.

import.py: used to create my application database tables (users, books, reviews) and inserting books.csv data into my books table along with the reviews_count and the average_rating that we take from the goodreads API. Also it will be noticed that the reviews table has a foreign key for the books (Many to One relation ship as many reviews are tied to a book) and also a foreign key to the users table as only 1 review is allowed for each user per book.

application.py: The whole backend logic is there! let's catagorize them by the routing.

("/"): sends you to the main page (unless you are not logged in and in that case redirected to the login page) and that's using the session id which equals the user's id. It is also responsible to send you to the book page (by checking the query of the url). Clears the session using the logout button and searchs for a book using datalist. Uses select sql statements to find all the books and add them to the datalist and does the same logic when you're sent to the book page and inserts data to the reviews table when you submit a review.

("/login): responsible for the login page logic. uses bcrypt.verify to decrypt the password in the database. Will send you to the main page if the username and password are correct otherwise will send you an error message.

("/register): very similar to the login page. will use bcrypt.encrypt to encrypt your password to the database. Will show an error message if the username that you try to register already exists.

("/api/<isbn>") responsible for sending json response regarding the book of that isbn otherwise will send response 404.
