#!/bin/python

class SimpleDatabase():
    def __init__(self):
        self.database = {}
        self.id_list = []

    def get_new_id(self):
        if not self.id_list:
            return 1
        
        return self.id_list[-1] + 1

    def log_new_id(self, id):
        self.id_list.append(id)

    def list(self):
        movie_list = []

        for entry in self.database.values():
            movie_list.append(entry)

        return movie_list

    def get_by_id(self, id):
        return self.database.get(id, None)

    def insert(self, title, release_year, description=None):
        new_id = self.get_new_id()
        movie_entry = {
            'id': new_id,
            'title': title,
            'release_year': release_year
        }

        if description:
            movie_entry['description'] = description
        self.database[new_id] = movie_entry
        self.log_new_id(new_id)

        return movie_entry

