from app.config.mysqlconnection import connectToMySQL

class User:
    """
    A user model representation.

    Attributes:
        id (int): The user ID.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
        created_at (datetime): The creation date and time.
        updated_at (datetime): The last update date and time.
    """
    def __init__(self, data):
        """
        Initializes the User object with the given data.

        Args:
            data (dict): The data dictionary containing user information. Expected keys are:
                - 'id': The user ID.
                - 'first_name': The user's first name.
                - 'last_name': The user's last name.
                - 'email': The user's email address.
                - 'created_at': The creation date and time.
                - 'updated_at': The last update date and time.
        """
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        """
        Gets all users from the database.

        Returns:
            list[User]: A list of User objects representing all users in the database.
        """
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        """
        Saves a new user to the database.

        Args:
            data (dict): The data dictionary containing user information. Expected keys are:
                - 'first_name': The user's first name.
                - 'last_name': The user's last name.
                - 'email': The user's email address.

        Returns:
            int: The ID of the newly created user.
        """
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s , %(last_name)s , %(email)s)"
        return connectToMySQL('users_schema').query_db(query, data)
