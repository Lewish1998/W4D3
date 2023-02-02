import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

# author_1 = Author('Terry', 'Pratchet')
# author_repository.save(author_1)
# author_2 = Author('Randolph', 'Lam')
# author_repository.save(author_2)

# book_1 = Book('The Colour Of Things Not Working', author_1)
# book_repository.save(book_1)
# book_2 = Book('Nation', author_1)
# book_repository.save(book_2)
# book_3 = Book('Python 4Eva', author_2)
# book_repository.save(book_3)

# book_repository.update(book_1)
# pdb.set_trace()