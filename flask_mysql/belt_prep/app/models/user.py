from __future__ import annotations

import re
from functools import wraps

from flask import flash, current_app, request, session, abort
from app.config.mysqlconnection import connectToMySQL

db = "recipes_schema"

class User:
    
    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data: dict) -> int|None:
        
        query = """
            INSERT INTO users (first_name, last_name, email, password) 
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        data["password"] = current_app.bcrypt.generate_password_hash(data["password"])
        result = connectToMySQL(db).query_db(query, data)

        return result if result else None
    
    @classmethod
    def get_by_id(cls, data: dict) -> User:

        query = "SELECT * FROM users WHERE id= %(id)s"

        result = connectToMySQL(db).query_db(query, data)

        return cls(result[0]) if result else None
    
    @classmethod
    def get_by_email(cls, data: dict) -> User:

        query = "SELECT * FROM users WHERE email = %(email)s"

        result = connectToMySQL(db).query_db(query, data)

        return cls(result[0]) if result else None
    
    @classmethod
    def update(cls, data: dict) -> None:
        
        query = """
            UPDATE users 
            SET first_name = %(first_name)s, last_name = %(last_name)s, email =  %(email)s
            WHERE id = %(id)s;
        """

        connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data: dict) -> None:

        query = "DELETE FROM users WHERE id = %(id)s"

        connectToMySQL(db).query_db(query, data)

    @classmethod
    def validate_registration(cls, data: dict):

        valid = True

        # Name validation:
        if len(data["first_name"]) < 2:
            flash("First name must be at least two characters long #reg", "danger")
            valid = False
        if len(data["last_name"]) < 2:
            flash("Last name must be at least two characters long #reg", "danger")
            valid = False

        # Email validation
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        exists = User.get_by_email({"email": data["email"]})
        if not bool(re.match(email_regex, data["email"])):
            flash("Invalid email format #reg", "danger")
            valid = False
        if exists:
            flash("Email already exists #reg", "danger")
            valid = False

        # Password validation
        if not data["password"] == data["confirm_password"]:
            flash("Passwords don't much #reg", "danger")
            valid = False

        return valid

    @staticmethod
    def validate_login(data: dict):
        
        valid = True

        user = User.get_by_email({"email": data["email"]})
        if not user:
            flash("Invalid credentials #log", "danger")
            valid = False
            return valid, user
        if not current_app.bcrypt.check_password_hash(user.password, data["password"]):
            flash("Invalid credentials #log", "danger")
            valid = False
    
        return valid, user
    

def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not "user_id" in session:
            abort(401)
        return func(*args, **kwargs)
    return decorator