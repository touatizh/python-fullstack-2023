from app.utils.validators import (Email, Password)
from flask_wtf import FlaskForm
from wtforms import (PasswordField, StringField, SubmitField)
from wtforms.validators import (DataRequired, Length, EqualTo)

class RegForm(FlaskForm):
    """
    Form class for user registration.

    This class represents a Flask-WTF form for registering a new user. It includes fields for 
    entering a first name, last name, email, password, and a password confirmation.

    Attributes:
        first_name (StringField): Input field for user's first name.
        last_name (StringField): Input field for user's last name.
        email (StringField): Input field for user's email. 
                             Validated for presence (DataRequired) and unique email and format using custom Email validator.
        password (PasswordField): Input field for user's password.
                                  Validated for presence (DataRequired), minimum length of 8, and specific password patterns.
        confirm_password (PasswordField): Input field to confirm the password.
                                          Validated for presence (DataRequired) and matching the original password.
        submit (SubmitField): Button to submit the registration form.
    """
    
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("Email", validators=[DataRequired(), Email(operation="register")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8), Password()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords don't match")])
    submit = SubmitField("Register")
