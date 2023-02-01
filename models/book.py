class Book:
    def __init__(self, title, author, id=None): # Author relates to the Author(s). id is books individual id
        self.title = title
        self.author = author
        self.id = id
