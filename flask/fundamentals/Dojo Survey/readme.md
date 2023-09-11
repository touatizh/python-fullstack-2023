# Coding Dojo Africa, full stack python course
# Assignement Dojo Survey

This project is a Flask web application that allows users to fill out a survey and view the submitted responses.

## Project Structure

- `app/`
  - `create_app.py`: Script to create and configure the Flask application.
  - `forms.py`: Defines WTForms forms and the respective field validations.
  - `routes.py`: Defines the routes for the Flask application and the respective view functions.
- `templates/`
  - `index.html`: Template for the survey form page.
  - `result.html`: Template to display the survey results.
- `static/`: Directory to store static files like CSS and JavaScript files.
- `run.py`: Script to create a Flask application instance and run the application.
- `requirements.txt`: File containing a list of all the Python packages required to run the application.
- `README.md`: This file, which provides an overview of the project and instructions for setting it up.

## Setup

1. Ensure that you have Python 3.6 or later installed.
2. Clone this repository: `git clone https://github.com/touatizh/python-fullstack-2023.git`
3. Navigate to the project directory: `cd python-fullstack-2023/flask/fundamentals/Dojo Survey`
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On MacOS/Linux: `source venv/bin/activate`
6. Install the required packages: `pip install -r requirements.txt`
7. Run the application in a development environment using the command: `python run.py`

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Fill out the survey form and submit it to view the results.

## Documentation

The project's codebase is thoroughly documented, including detailed docstrings for classes and functions, and comments explaining different sections of code. This documentation facilitates a deeper understanding of the application's workings and serves as a valuable reference point.

For a detailed breakdown of the project's structure and functionalities, refer to the docstrings in the Python scripts.

## Acknowledgements

- Flask, a lightweight WSGI web application framework in Python.
- WTForms, a flexible forms validation and rendering library for Python web development.

## Contact

[Helmi Touati](mailto:touatizh@gmail.com)

