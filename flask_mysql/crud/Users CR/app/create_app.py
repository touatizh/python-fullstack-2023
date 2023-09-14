from flask import Flask
from .urls import bp
import os

# Define the base and current directories using the os module to construct paths for the template and static folders
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

def create_app() -> Flask:
    """
    Creates and configures the Flask application.

    This function creates a Flask application with configured template and static file directories. 
    It also registers a blueprint to organize the application's routes.

    Returns:
        Flask: The initialized and configured Flask application.
    """

    # Create the Flask application with custom template and static folders based on the project's base directory
    app = Flask(__name__, 
                template_folder=os.path.join(BASE_DIR, "templates"),
                static_folder=os.path.join(BASE_DIR, "static"))

    # Register the blueprint to add the routes to the application
    app.register_blueprint(bp)

    return app
