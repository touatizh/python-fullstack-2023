import re

from app.models.users import User
from flask_wtf import FlaskForm
from wtforms.fields.core import Field
from wtforms.validators import ValidationError

from flask import flash


class Email:
    """
    A validator class for email validation based on the operation context.

    This class provides a callable validator for WTForms fields. It validates the email's format and, 
    based on the operation context, ensures either uniqueness (for registration) or existence (for login) 
    of the email in the system.

    Attributes:
        operation (str): The context in which validation is performed. Valid values are 'register' and 'login'.

    """
    def __init__(self, operation: str = "register") -> None:
        """
        Initializes the Email validator with the specified operation context.

        Args:
            operation (str, optional): The context for validation. Defaults to "register".
        """
        self.operation = operation
    
    def __call__(self, form: FlaskForm, email: Field) -> None:
        """
        The main validation method called by WTForms during form validation.

        This method checks the email format using a regex pattern. Depending on the operation context, 
        it also verifies the email's uniqueness or existence in the system.

        Args:
            form (FlaskForm): The form containing the email field.
            email (Field): The email field to be validated.

        Raises:
            ValidationError: If the email fails the validation checks. Specific error messages are flashed 
                             to inform the user.
            Exception: If an invalid operation context is provided.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not bool(re.match(email_regex, email.data)):
            flash("Invalid email format. #reg", "danger")
            raise ValidationError

        exists = User.get_by_email({"email": email.data})

        match self.operation:
            case "register":
                if exists:
                    flash("A user with the same email already exists. #reg", "danger")
                    raise ValidationError
            case "login":
                if not exists:
                    flash("Invalid credentials. #login", "danger")
                    raise ValidationError
            case _:
                flash("Internal Server Error.", "danger")
                raise Exception("Invalid email validation operation")

class Password:
    """
    A validator class for password validation based on the operation context.

    This class provides a callable validator for WTForms fields. It checks the provided password for specific patterns, ensuring it meets the required criteria based on the operation context (e.g., "register").

    Attributes:
        operation (str): The context in which the validator is used. Valid values are 'register' and 'login'.

    Raises:
        ValidationError: If the password does not meet the specified criteria.
        Exception: If an invalid operation is provided.
    """

    def __init__(self, operation: str = "register") -> None:
        """
        Initializes the Password validator with the specified operation context.

        Args:
            operation (str): The context in which the validator is used. Defaults to 'register'.
        """
        self.operation = operation

    def __call__(self, form: FlaskForm, password: Field) -> None:
        """
        Validates the provided password based on the operation context.

        For the 'register' context, the password is checked against specific patterns.
        For the 'login' context, the validation is pending further implementation.

        Args:
            form (FlaskForm): The form containing the password field.
            password (Field): The password field to validate.

        Raises:
            ValidationError: If the password does not meet the specified criteria.
        """
        match self.operation:
            case "register":
                patterns = [
                    (r'[a-zA-Z]', "Password must include at least one letter (a-z or A-Z). #reg"),
                    (r'[0-9]', "Password must include at least one number (0-9). #reg"),
                    (r'[!@#$%^&*()_+=-]', "Password must include at least one symbol (!@#$%^&*()_+=-). #reg"),
                    (r'[^a-zA-Z0-9!@#$%^&*()_+=-]', "Make sure you include letters (a-z or A-Z), numbers (0-9), and symbols (!@#$%^&*()_+=-) only. #reg")
                ]

                valid = True

                for pattern, message in patterns:
                    if (pattern == r'[^a-zA-Z0-9!@#$%^&*()_+=-]' and re.search(pattern, password.data)) or \
                    (pattern != r'[^a-zA-Z0-9!@#$%^&*()_+=-]' and not re.search(pattern, password.data)):
                        flash(message, "danger")
                        valid = False

                if not valid:
                    raise ValidationError
            case "login":
                #TODO to be done after implementing password hashing
                pass
            case _:
                flash("Internal Server Error.", "danger")
                raise Exception("Invalid email validation operation")
