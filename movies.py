#!/bin/python

from flask import Flask
import requests
import json
import sqlite3

app = Flask(__name__)

class DatabaseAccess:
    def __init__(self):
        self.con = sqlite3.connect("movies.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE movie(id, title, description, release_year)")

    def get_database(self):
        res = self.cur.execute("SELECT * FROM movies")
        records = res.fetchone()
        for row in records:
            print("id: ", row[0])
            print("title: ", row[1])
            print("description: ", row[2])
            print("release_year: ", row[3])

    def get_by_id(self, id):
        res = self.cur.execute(f"SELECT * FROM movies WHERE movies.id = {id}")
        record = res.fetchone()
        print("id: ", record[0])
        print("title: ", record[1])
        print("description: ", record[2])
        print("release_year: ", record[3])

    def insert(self, id, title, descr, releas_year):
        self.cur.execute(f"""INSERT INTO movie VALUES
                        ({id}, {title}, {descr}, {releas_year})""")

@app.route("/")

def index():
    table = DatabaseAccess{1, "Matrix", "SFFDF", 2020}
    result = json.dumps(result)
    return result

if __name__ == '__main__':
    app.run()