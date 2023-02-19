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
            result = json.dumps(row, indent = 2)
        return result

    def get_by_id(self, id):
        res = self.cur.execute(f"SELECT * FROM movies WHERE movies.id = {id}")
        record = res.fetchone()
        return json.dumps(record, indent = 2)

    def control(self):
        pass
    
    def insert(self, id, title, descr, releas_year):
        self.cur.execute(f"""INSERT INTO movie VALUES
                        ({id}, {title}, {descr}, {releas_year})""")


@app.route("/")
def index():
    database = sqlite3.connect("movies.db")
    _ = DatabaseAccess(database)
    
    


if __name__ == '__main__':
    app.run()
