import pdb
from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import author_repository
from repositories import book_repository
from models.book import Book
from models.author import Author

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

@library_blueprint.route('/books/add-author', methods=['GET'])
def new_author():
    return render_template('/books/add-author.html')



# New author
@library_blueprint.route('/authors', methods=['POST'])
def create_author():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    author_repository.save(Author(first_name, last_name))
    return redirect('/authors')


# show author
@library_blueprint.route('/authors/<id>', methods=['GET'])
def show_author(id):
    author = author_repository.select(id)
    # books = book_repository.select_all()
    return render_template('books/show-author.html', author=author)




# delete author
@library_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_author(id):
    author_repository.delete(id)
    return redirect('/books')



# New task
# get request
@library_blueprint.route('/books/add', methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template('books/add.html', authors = authors)

# create task
# post request
@library_blueprint.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
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

# edit book
@library_blueprint.route('/books/<id>/edit', methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book=book, authors=authors)







# update book - why wont you work??????????????
@library_blueprint.route('/books/<id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    test = author.first_name, author.last_name, author.id
    print(author.first_name) # able to print author id but not first name??
    book = Book(title, author.id, id)

    # print(book.author.id) # still able to access this
    # Can't adapt type Author 


#     # most recent error: column "author" is of type integer but expression is of type record
# LINE 1: UPDATE books SET (title, author) = ('Nation', ('Randolph', '...
# HINT:  You will need to rewrite or cast the expression.


    book_repository.update(book)
    return redirect('/books')







# delete book
@library_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
