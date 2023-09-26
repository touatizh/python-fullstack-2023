import os
from app.config.mysqlconnection import connectToMySQL

db = os.environ.get("DB")

class Ninja:
    """
    Represents a Ninja with attributes and methods for database interactions.
    
    Attributes:
        id (int): Unique identifier for the ninja.
        first_name (str): First name of the ninja.
        last_name (str): Last name of the ninja.
        dojo_id (int): ID of the dojo associated with the ninja.
        created_at (datetime): Timestamp when the ninja was created.
        updated_at (datetime): Timestamp of the last update to the ninja's data.
    """

    def __init__(self, data: dict) -> None:
        """
        Initialize a new Ninja instance.

        Args:
            data (dict): Dictionary containing the ninja's details. Expected keys:
                - 'id': The ninja's ID.
                - 'first_name': The ninja's first name.
                - 'last_name': The ninja's last name.
                - 'dojo_id': The ID of the ninja's dojo.
                - 'created_at': Timestamp when the ninja was created.
                - 'updated_at': Timestamp of the last update to the ninja's data.
        """
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data: dict) -> int:
        """
        Saves a new ninja to the database.

        Args:
            data (dict): The data dictionary containing ninja information. Expected keys:
                - 'first_name': The ninja's first name.
                - 'last_name': The ninja's last name.
                - 'dojo_id': The ID of the ninja's dojo.
                - 'age': The age of the ninja.

        Returns:
            int: The ID of the newly created ninja.
        """
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        return connectToMySQL(db).query_db(query, data)
