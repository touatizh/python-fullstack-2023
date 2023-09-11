from flask import Flask
from .routes import bp
import os

# Base project directory for reference
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

def create_app() -> Flask:
    app = Flask(__name__, 
                template_folder=os.path.join(BASE_DIR, "templates"),
                static_folder=os.path.join(BASE_DIR, "static"))

    app.register_blueprint(bp)

    return app
