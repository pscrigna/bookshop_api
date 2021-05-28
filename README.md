Flask API - ABM of Books

* Welcome message.

curl http://localhost:5000/home -X GET

* Query a book. 

curl http://localhost:5000/book/6 -X GET

* Query all the books.

curl http://localhost:5000/book/list -X GET

* Delete a book.

curl http://localhost:5000/book/2 -X DELETE

* Add a new book.

curl -H "Content-Type: application/json" -X POST -d '{"title":"Read a book", "author":"Bob","isbn":"33", "price":"3.44"}' http://localhost:5000/book

* Update a book.

curl -H "Content-Type: application/json" -X PUT -d '{"title":"Read a Python Book", "author":"Bob Jones","isbn":"33", "price":"93.44"}' http://localhost:5000/book



