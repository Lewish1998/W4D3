from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import author_repository
from repositories import book_repository
from models.book import Book

library_blueprint = Blueprint('books', __name__)

@library_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', books=books)






# New task
# get request
@library_blueprint.route('/library/new', methods=['GET'])
def new_book():
    books = book_repository.select_all()
    return render_template('library/new.html', all_books = books)

# create task
# post request


# show task
# get request


# edit task
# get request

# update task
# post request 


# delete task
# post request 