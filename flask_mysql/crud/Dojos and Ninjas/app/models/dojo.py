from __future__ import annotations
import os
from app.config.mysqlconnection import connectToMySQL

db = os.environ.get("DB")

class Dojo:
    """
    Represents a Dojo with methods to interact with the database.
    
    Attributes:
        id (int): The ID of the dojo.
        name (str): The name of the dojo.
        created_at (datetime): The creation timestamp of the dojo.
        updated_at (datetime): The last update timestamp of the dojo.
    """
    def __init__(self, data: dict) -> None:
        """
        Initializes the Dojo object with given data.
        
        Args:
            data (dict): A dictionary containing data about the dojo. Expected keys:
                - 'id': The ID of the dojo.
                - 'name': The name of the dojo.
                - 'created_at': The creation timestamp of the dojo.
                - 'updated_at': The last update timestamp of the dojo.
        """
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls) -> list[Dojo]:
        """
        Gets all dojos from the database.

        Returns:
            list[Dojo]: A list of Dojo objects representing all dojos in the database.
        """
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)

        dojos = [cls(dojo) for dojo in results]
        return dojos
    
    @classmethod
    def get_by_id(cls, data: dict) -> Dojo:
        """
        Retrieves a dojo from the database using its id.

        Args:
            data (dict): A dictionary containing the id of the dojo to retrieve. Expected keys:
                - 'id': The ID of the dojo.

        Returns:
            Dojo: A Dojo object representing the dojo with the given id in the database.
        """
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        results = connectToMySQL(db).query_db(query, data)

        return cls(results[0])

    @classmethod
    def save(cls, data: dict) -> int:
        """
        Saves a new dojo to the database.

        Args:
            data (dict): The data dictionary containing dojo information. Expected keys:
                - 'name': The dojo's name.

        Returns:
            int: The ID of the newly created dojo.
        """
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_ninjas(cls, data: dict) -> list[dict]:
        """
        Retrieves ninjas associated with a specific dojo from the database.

        Args:
            data (dict): A dictionary containing the id of the dojo. Expected keys:
                - 'id': The ID of the dojo.

        Returns:
            list[dict]: A list of dictionaries where each dictionary contains information about a ninja.
        """
        query = "SELECT first_name, last_name, age FROM ninjas LEFT JOIN dojos ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"

        return connectToMySQL(db).query_db(query, data)
