from __future__ import annotations

from flask import flash, current_app
from app.config.mysqlconnection import connectToMySQL
from app.models.user import User

db = "recipes_schema"

class Recipe:

    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_thirty = data["under_thirty"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
    
    @classmethod
    def create(cls, data: dict) -> int|None:

        query = """
            INSERT INTO recipes (name, description, instructions, date_made, under_thirty, user_id) 
            VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, b%(under_thirty)s, %(user_id)s);
        """
        result = connectToMySQL(db).query_db(query, data)
        return result if result else None
    
    @classmethod
    def get_by_id(cls, data: dict) -> Recipe:

        query = "SELECT * FROM recipes WHERE id= %(id)s"

        result = connectToMySQL(db).query_db(query, data)
        if result:
            recipe = cls(result[0])
            recipe.user = User.get_by_id({"id": result[0]["user_id"]})
            recipe.under_thirty = bool(recipe.under_thirty == b'\x01')
            return recipe
    
    @classmethod
    def get_all(cls) -> Recipe|None:

        recipes = []
        query = "SELECT * FROM recipes;"

        results = connectToMySQL(db).query_db(query)
        if results:
            for result in results:
                recipe = cls(result)
                recipe.under_thirty = bool(recipe.under_thirty == b'\x01')
                recipe.user = User.get_by_id({"id": result["user_id"]})
                recipes.append(recipe)
            return recipes

    @classmethod
    def update(cls, data: dict) -> None:
        
        query = """
            UPDATE recipes 
            SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_thirty = b%(under_thirty)s
            WHERE id = %(id)s;
        """

        connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data: dict) -> None:

        query = "DELETE FROM recipes WHERE id = %(id)s"

        connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_data(data: dict) -> bool:

        valid = True

        for value in data.values():
            if not value:
                valid = False
                flash("All fields must contain valid data", "danger")
                return valid

        for key, value in data.items():
            if key in ["name", "description", "instructions"] and len(value) < 3:
                valid = False
                flash(f"Field {key} must be at least 3 characters long")

        return valid