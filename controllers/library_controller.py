from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import author_repository
from repositories import book_repository
from models.book import Book

library_blueprint = Blueprint('books', __name__)

@library_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    authors = author_repository.select_all()
    return render_template('books/books.html', books=books, authors=authors)


@library_blueprint.route('/authors')
def authors():
    authors = author_repository.select_all()
    return render_template('books/authors.html', authors=authors)

# New task
# get request
@library_blueprint.route('/add', methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template('books/add.html', authors = authors)

# create task
# post request
@library_blueprint.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    # author_id = request.form['author_id']
    author = author_repository.select(request.form['author_id'])
    book = Book(title, author)
    book_repository.save(book)
    return redirect ('/books')

# show task
# get request
@library_blueprint.route('/books/<id>', methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/show.html', book=book, authors=authors)

# edit task
# get request

# update task
# post request 


# delete task
# post request 
@library_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
