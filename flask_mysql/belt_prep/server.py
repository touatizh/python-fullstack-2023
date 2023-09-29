from app import app
from app.controllers import users, recipes

if __name__ == "__main__":
    """
    Entry point for running the Flask application.
    
    Checks if the script is being run as the main module and then starts the Flask application with debugging enabled.
    """
    app.run(debug=True)