class SimpleDatabase():
    """Simple class of movie database, based on basic python dictionaries
    """
    def __init__(self):
        self.database = {}
        self.id_list = []

    def get_new_id(self):
        """For 'POST' command to give new movie his id
         when it`s uploaded to database

        Returns:
            int: New id for new movie
        """
        if not self.id_list:
            return 1

        return self.id_list[-1] + 1

    def log_new_id(self, id):
        """Adds id to list that new id for new movie could be created

        Args:
            id (int): id of last added movie
        """
        self.id_list.append(id)

    def list(self):
        """List of all movies

        Returns:
            List: List of all movies in database
        """
        movie_list = []

        for entry in self.database.values():
            movie_list.append(entry)

        return movie_list

    def get_by_id(self, id):
        """Find movie by his id

        Args:
            id (int): id of wanted movie

        Returns:
            dict: wanted movie
        """
        return self.database.get(id, None)

    def insert(self, title, release_year, description=None):
        """Insert new movie to table

        Args:
            title (str): Title of movie
            release_year (int): release year of movie
            description (str, optional): description of movie. Defaults to None.

        Returns:
            dict: new movie
        """
        new_id = self.get_new_id()
        movie_entry = {
            'id': new_id,
            'title': title,
            'release_year': release_year
        }
#If description is given add it into the table
        if description:
            movie_entry['description'] = description
        self.database[new_id] = movie_entry
        self.log_new_id(new_id)

        return movie_entry

    def update(self, id, changes):
        """Upload changes into the table to specific movie

        Args:
            id (int): id of movie which is wanted to be changed
            changes (dict): List of changes wanted to be done

        Returns:
            dict: Upload movie with changes
        """
        entry = self.database.get(id, None)

        if not entry:
            return None

        title = changes.get('title', None)
        release_year = changes.get('release_year', None)
        desc = changes.get('description', None)

        if title:
            entry['title'] = title
        if release_year:
            entry['release_year'] = release_year
        if desc:
            entry['description'] = desc

        return entry
