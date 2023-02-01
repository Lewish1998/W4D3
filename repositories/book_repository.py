from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import pdb

def save(book):
    sql = 'INSERT INTO books (title, author) VALUES (%s, %s) RETURNING *'
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = 'SELECT * FROM books'
    results = run_sql(sql)
    for row in results:
        book = Book(row['title'], row['author'], row['id'])
        books.append(book)
    return books

def select(id):
    book = []
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    # pdb.set_trace()
    result = run_sql(sql, values)[0]
    if result is not None:
        book = Book(result['title'], result['author'], result['id'])
    return book

def delete_all():
    sql = 'DELETE FROM books'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM books WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = 'UPDATE books SET (title, author) = (%s, %s) WHERE id = %s'
    values = [book.title, book.author, book.id]
    run_sql(sql, values)