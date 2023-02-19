#GET/movies
**This function will return whole table. If table is empty it will return empty list**

`curl -X GET localhost:5000/movies`


#POST/movie
**This function will check if movie wanted to be add has got the correct components/arguments, if yes it will add new movie into the table**

`curl -X POST localhost:5000/movies -H 'Content-Type: application/json' -d '{"title":"Matrix","description":"Movie with Keanu Reeves","release_year":1999}'`

#GET/movie/<int:id>
**This function will return movie (id, title, description, release year) with wanted id**

`curl -X GET localhost:5000/movies/1`

#PUT/movie/<int:id>
**This function will change components of wanted movie (by id), and return it with new ones**

`curl -X PUT localhost:5000/movies/1 -H 'Content-Type: application/json' -d '{"title":"John Wick","release_year":2014}'`
