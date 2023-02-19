#!/bin/python

import sqlite3

class DatabaseAccess:
    def __init__(self):
        self.con = sqlite3.connect("movies.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE movie
            (id integer primary key, title text,
            description text, release_year integer)""")
        self.con.commit()

        self.id_list = []

    def get_new_id(self):
        if not self.id_list:
            return 1
        return self.id_list[-1] + 1

    def log_new_id(self, id):
        self.id_list.append(id)

    def get_database(self):
        res = self.cur.execute("SELECT * FROM movies")
        records = res.fetchone()

        return [row for row in records]

    def get_by_id(self, id):
        res = self.cur.execute(f"""SELECT * FROM movies
                                WHERE movies.id = {id}""")
        record = res.fetchone()
        return record

    def control(self, title, descr, year):
        if title is str and descr is str and year is int:
            new_id = 1
            while self.cur.execute(f"""SELECT * FROM movies
                                   WHERE movies.id = {new_id}""") is not None:
                new_id += 1
            self.insert(new_id, title, descr, year)
        else:
            return "Bad request status code"

    def insert(self, id, title, descr, releas_year):
        if id is None:
            id = self.get_new_id()
        self.cur.execute(f"""INSERT INTO movie VALUES
                        ({id}, {title}, {descr}, {releas_year})""")
        self.con.commit()
        self.log_new_id(id)
        return self.get_by_id(id)
