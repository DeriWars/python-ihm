from sqlite3 import *

class UserDatabase():
    """
    The users database.
    Store the name and password of the user.
    """
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        """
        Create the users' table.
        """
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                            name TEXT,
                            password TEXT)""")
        self.conn.commit()
    
    def add_user(self, username: str, password: str):
        """
        Add a user to the database.

        Args:
            username (str): the user's name
            password (str): the user's encrypted password
        """
        
        self.cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        self.conn.commit()
    
    def get_user(self, username: str) -> dict:
        """
        Search for a user in the database by name.

        Args:
            username (str): the user's name

        Returns:
            dict: the user's information or None if not found.
        """
        
        self.cursor.execute("SELECT * FROM users WHERE name=?", (username,))
        return self.cursor.fetchone()
    
    def is_valid_user(self, username: str, password: str) -> bool:
        """
        Check if the user is valid.
        
        Params:
            username (str): the user's name
            password (str): the user's encrypted password
        
        Returns:
            bool: True if the user is valid, False otherwise.
        """
        
        self.cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (username,password,))
        return self.cursor.fetchone() is not None