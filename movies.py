#!/bin/python

from flask import Flask
import sqlite3
import json

app = Flask(__name__)


class DatabaseAccess:
    def __init__(self):
        self.cur = self.cursor()
        self.cur.execute("""CREATE TABLE movie
                        (id integer, title text, 
                        description text, release_year integer)""")

    def get_database(self):
        res = self.cur.execute("SELECT * FROM movies")
        records = res.fetchone()
        for row in records:
            json.dumps(row, indent = 2)

    def get_by_id(self, id):
        res = self.cur.execute(f"SELECT * FROM movies WHERE movies.id = {id}")
        record = res.fetchone()
        json.dumps(record, indent = 2)

    def insert(self, id, title, descr, releas_year):
        self.cur.execute(f"""INSERT INTO movie VALUES
                        ({id}, {title}, {descr}, {releas_year})""")


@app.route("/")
def index():
    database = sqlite3.connect("movies.db")
    work_place = DatabaseAccess(database)
    work_place.get_database()
    


if __name__ == '__main__':
    app.run()
