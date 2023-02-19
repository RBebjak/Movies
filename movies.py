#!/bin/python

from flask import Flask, Response, request, jsonify

from simple_database import SimpleDatabase


app = Flask(__name__)
db = SimpleDatabase()

BAD_REQUEST = ('Bad Request', 400)
NOT_FOUND = ('Not Found', 404)


@app.route('/movies', methods=['GET'])
def get_movies():
    movies = db.list()
    return jsonify(movies)


@app.route('/movies', methods=['POST'])
def upload_movie():
    movie = request.json

    if not __check_post__(movie.keys()):
        return Response(
            BAD_REQUEST[0],
            status=BAD_REQUEST[1]
        )

    if movie.get('description', ""):
        new_movie = db.insert(
            movie.get('title'),
            movie.get('release_year'),
            movie.get('description')
        )
    else:
        new_movie = db.insert(
            movie.get('title'),
            movie.get('release_year')
        )

    return jsonify(new_movie)


def __check_post__(post_keys):
    required_keys = ('title', 'release_year')

    for key in required_keys:
        if key not in post_keys:
            return False

    return True

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = db.get_by_id(movie_id)

    if not movie:
        return Response(
            NOT_FOUND[0],
            status=NOT_FOUND[1]
        )

    return jsonify(movie)


if __name__ == '__main__':
    app.run()
