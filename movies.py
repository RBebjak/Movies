#!/bin/python

from flask import Flask, request, jsonify
import json
from.database_movies import DatabaseAccess

app = Flask(__name__)

database = DatabaseAccess()

@app.route("/movies", methods = ['GET'])
def get_movie():
    movie = database.get_database()

    return jsonify(movie)

@app.route("/movies", methods = ['POST'])
def post_movie():
    movie = request.

if __name__ == '__main__':
    app.run()
