from flask import Flask
import bookdb
from flask import render_template

app = Flask(__name__)

db = bookdb.BookDB()


@app.route('/')
def books():
    # put code here that provides a list of books to a template named 
    # "book_list.html"
    books = db.titles()
    return render_template('book_list.html', book_list=books)


@app.route('/book/<book_id>/')
def book(book_id):
    # put code here that provides the details of a single book to a template 
    # named "book_detail.html"
    
    return render_template('book_detail.html', book=db.title_info(book_id))


if __name__ == '__main__':
    app.run(debug=True)
