from flask.json import JSONEncoder

import csv


class Book:
    """  Describe a book characteristics  """
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return str(self.isbn) + ' - ' + self.title + ' by ' + self.author +\
             ' @ ' + str(self.price)


class Bookshop:
    """ Represents the API functions """
    def __init__(self, file):
        self.books = []
        self.file = file

    def delete_book(self, isbn):
        result = False
        with open(self.file, 'r', newline='') as csvfile:
            reader = list(csv.reader(csvfile))

        with open(self.file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for book in reader:
                if int(book[0]) != isbn:
                    writer.writerow(book)
                else:
                    result = True
        return result

    def get_book(self, isbn):
        with open(self.file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for x in reader:
                if int(x[0]) == isbn:
                    return Book(int(x[0]), x[1], x[2], x[3])
        return Book('0', 'No existe el isbn', '', '0.00')

    def add_book(self, book):
        with open(self.file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([book.isbn, book.title, book.author, book.price])

    def list_books(self):
        with open(self.file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for book in reader:
                self.books.append(Book(book[0], book[1], book[2], book[3]))
        return self.books

    def update_book(self, isbn, title, author, price):
        if self.delete_book(int(isbn)) is True:
            self.add_book(Book(isbn, title, author, price))
            return True
        else:
            return False


class BookJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'isbn': obj.isbn,
                'Titulo': obj.title,
                'Autor': obj.author,
                'Precio': obj.price
            }
        else:
            return super(BookJSONEncoder, self).default(obj)
