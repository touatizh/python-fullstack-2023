from flask import Flask
import os

# Define the base and current directories using the os module to construct paths for the template and static folders
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

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
                template_folder=os.path.join(CURRENT_DIR, "templates"),
                static_folder=os.path.join(CURRENT_DIR, "static"))

    # Set secret key
    app.secret_key = os.environ.get("SECRET_KEY")

    return app
