from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class UserForm(FlaskForm):
    """
    A form for collecting user information.

    This form collects the user's first name, last name, and email. The email field is
    validated to ensure it is provided and that it meets the criteria of a valid email
    address.

    Attributes:
        first_name (StringField): The user's first name. Label: "First Name:".
        last_name (StringField): The user's last name. Label: "Last Name:".
        email (StringField): The user's email. Label: "Email:". Validated to be a non-empty valid email address.
        submit (SubmitField): The form submission button. Label: "Submit".
    """
    first_name = StringField(label="First Name:")
    last_name = StringField(label="Last Name:")
    email = StringField(label="Email:", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")
