from __future__ import annotations
import os

from flask import flash, current_app
from app.config.mysqlconnection import connectToMySQL

db = os.environ.get("DB")

class User:
    """
    Represents a user entity and provides methods to interact with the database.

    The User class encapsulates the attributes of a user and provides class methods
    for database operations like fetching a user by email and saving a new user.

    Attributes:
        id (int): The user's ID.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
        password (str): The user's hashed password.
        date_of_birth (str): The user's date of birth. #TODO to be implemented on bonus tasks
        gender (str): The user's gender. #TODO to be implemented on bonus tasks
        created_at (str): The datetime the user was created.
        updated_at (str): The datetime the user was last updated.
    """
    
    def __init__(self, data: dict) -> None:
        """
        Initializes the User object with the provided data.

        Args:
            data (dict): A dictionary containing key-value pairs for user attributes.
        """
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.date_of_birth = data["date_of_birth"]
        self.gender = data["gender"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_by_email(cls, data: dict) -> User|None:
        """
        Fetches a user from the database based on the provided email.

        Args:
            data (dict): A dictionary containing the email of the user to be fetched.

        Returns:
            User|None: Returns a User object if found, otherwise None.
        """
        query = "SELECT * FROM users WHERE email=%(email)s"

        results = connectToMySQL(db).query_db(query, data)

        if results:
            return results[0]

    @classmethod
    def save(cls, data: dict) -> int:
        """
        Saves a new user to the database and returns the user's ID.

        Args:
            data (dict): A dictionary containing the user's details to be saved.

        Returns:
            int: The ID of the saved user.
        """
        data["password"] = current_app.bcrypt.generate_password_hash(data["password"])
        
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        
        result = connectToMySQL(db).query_db(query, data)
        if result:
            flash("Registered successfully. #reg", "info")
            return result
