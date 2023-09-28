# Coding Dojo Africa, full stack python course
# Assignement Login and Registration

This project is a Flask web application that allows users register a new user to the database and manage login and logout operations.

## Project Structure

- `app/`
  - `config`
    - `mysqlconnection.py`: Configuration script for connecting to the MySQL database.
  - `controllers/`
    - `forms.py`: Defines WTForms forms for registration and login.
    - `urls.py`: Defines the URL patterns for the application.
    - `views.py`: Contains the view functions for handling different routes.
  - `models`
    - `users.py`: Defines the User model and related database interactions.
  - `templates/`
    - `dashboard.html`: Template that only an authenticated user can access.
    - `index.html`: Template for main landing page that displays register and login forms.
    - `layout.html`: Base template that other templates inherit from.
  - `static/`: Directory to store static files like CSS and JavaScript files (if any).
  - `create_app.py`: Script to create and configure the Flask application.
- `run.py`: Script to create a Flask application instance and run the application.
- `Pipfile`: Contains a list of Python packages required to run the application.
- `Pipfile.lock`: Contains the exact versions and dependencies of the packages listed in the Pipfile.
- `README.md`: This file, which provides an overview of the project and instructions for setting it up.

## Setup

1. Ensure that you have Python 3.10 or later installed due to the use of "Match...Case" statement.
2. Ensure that you have pipenv install: `pip install pipenv`
3. Clone this repository: `git clone https://github.com/touatizh/python-fullstack-2023.git`
4. Navigate to the project directory: `cd python-fullstack-2023/flask_mysql\validation\Login and Registration`
5. Install the required dependencies: `pipenv install`
6. Ensure that you have a `.env` file under project directory containing the following environment variables:
    - HOST: pymysql connection host
    - USER: pymysql connection user
    - PASSWORD: USER's password
    - DB: name of the database for the project
    - SECRET_KEY: Flask app secret key
7. Run the application using the commands: `pipenv shell` followed by `python run.py`

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Register users, login and logout as you wish.

## Documentation

The project's codebase is thoroughly documented, including detailed docstrings for classes and functions. This documentation facilitates a deeper understanding of the application's workings and serves as a valuable reference point.

For a detailed breakdown of the project's structure and functionalities, refer to the docstrings in the Python scripts.

## Acknowledgements

- Flask, a lightweight WSGI web application framework in Python.
- WTForms, a flexible forms validation and rendering library for Python web development.
- Flask-Bcrypt, an extension that provides bcrypt hashing utilities for Flask applications.
- PyMySQL, a pure Python MySQL client that allows you to interface with MySQL database seamlessly.

## Contact

[Helmi Touati](mailto:touatizh@gmail.com)

