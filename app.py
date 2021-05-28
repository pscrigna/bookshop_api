from flask import Flask, jsonify, request, abort
from book import BookJSONEncoder, Bookshop, Book


def create_bookshop_service():
    app = Flask(__name__)
    app.json_encoder = BookJSONEncoder

    @app.route('/book/list', methods=['GET'])
    def get_books():
        books = Bookshop('libros.csv')
        return jsonify({'Libros': books.list_books()})

    @app.route('/book/<int:isbn>', methods=['GET'])
    def get_book(isbn):
        books = Bookshop('libros.csv')
        book = books.get_book(isbn)
        return jsonify({'Libro': book})

    @app.route('/home', methods=['GET'])
    def welcome():
        return jsonify({'msg': 'Welcome to SF Library!!!!'})

    @app.route('/book', methods=['POST'])
    def new_book():
        if not request.json or 'isbn' not in request.json:
            abort(400)
        book = Book(request.json['isbn'], request.json['title'],
                    request.json.get('author', ""),
                    float(request.json['price']))
        b = Bookshop('libros.csv')
        b.add_book(book)
        return jsonify({'Libro': book}), 201

    @app.route('/book', methods=['PUT'])
    def update_book():
        if not request.json or 'isbn' not in request.json:
            abort(400)
        book = Bookshop('libros.csv')
        result = book.update_book(request.json['isbn'],
                                  request.json['title'],
                                  request.json['author'],
                                  request.json['price'])
        return jsonify({'result': result}), 201

    @app.route('/book/<int:isbn>', methods=['DELETE'])
    def delete_book(isbn):
        b = Bookshop('libros.csv')
        result = b.delete_book(isbn)
        return jsonify({'result': result})

    return app


if __name__ == "__main__":
    app = create_bookshop_service()
    app.run(debug=True)
