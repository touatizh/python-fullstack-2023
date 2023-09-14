from flask import Blueprint
from . import views

# Create a new Blueprint object to define routes for the user creation and retrieval
bp = Blueprint("user_cr", __name__)

# Define a route for the index page, binding it to the index view function from the views module
bp.add_url_rule("/", "index", view_func=views.index)
# Define a route for the user creation page, binding it to the add_new_user view function from the views module
# This route supports both GET and POST methods to allow for user creation form submissions
bp.add_url_rule("/users/new", "add_user", view_func=views.add_new_user, methods=["GET", "POST"])
