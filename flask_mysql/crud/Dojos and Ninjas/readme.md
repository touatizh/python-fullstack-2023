# Coding Dojo Africa, full stack python course
# Assignement Dojos and Ninjas

This project is a Flask web application that allows users to manage Dojos and associated Ninjas.

## Project Structure

- `app/`
  - `config`
    - `mysqlconnection.py`: Configuration script for connecting to the MySQL database.
  - `controllers/`
    - `forms.py`: Defines WTForms forms for Ninjas and Dojos.
    - `urls.py`: Defines the URL patterns for the application.
    - `views.py`: Contains the view functions for handling different routes.
  - `models`
    - `dojo.py`: Defines the Dojo model and related database interactions.
    - `ninja.py`: Defines the Ninja model and related database interactions.
  - `templates/`
    - `add_ninja.html`: Template for adding a new ninja.
    - `dojo.html`: Template for displaying a dojo and its associated ninjas.
    - `index.html`: Template for main landing page that displays a form a to add a new dojo and a list of all dojos in database.
    - `layout.html`: Base template that other templates inherit from.
  - `static/`: Directory to store static files like CSS and JavaScript files (if any).
  - `create_app.py`: Script to create and configure the Flask application.
- `run.py`: Script to create a Flask application instance and run the application.
- `Pipfile`: Contains a list of Python packages required to run the application.
- `Pipfile.lock`: Contains the exact versions and dependencies of the packages listed in the Pipfile.
- `README.md`: This file, which provides an overview of the project and instructions for setting it up.

## Setup

1. Ensure that you have Python 3.6 or later installed.
2. Ensure that you have pipenv install: `pip install pipenv`
3. Clone this repository: `git clone https://github.com/touatizh/python-fullstack-2023.git`
4. Navigate to the project directory: `cd python-fullstack-2023/flask_mysql\crud\Dojos and Ninjas`
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
2. Create and display dojos and ninjas.

## Documentation

The project's codebase is thoroughly documented, including detailed docstrings for classes and functions. This documentation facilitates a deeper understanding of the application's workings and serves as a valuable reference point.

For a detailed breakdown of the project's structure and functionalities, refer to the docstrings in the Python scripts.

## Acknowledgements

- Flask, a lightweight WSGI web application framework in Python.
- WTForms, a flexible forms validation and rendering library for Python web development.
- PyMySQL, a pure Python MySQL client that allows you to interface with MySQL database seamlessly.

## Contact

[Helmi Touati](mailto:touatizh@gmail.com)

