from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from app.models.dojo import Dojo

class DojoForm(FlaskForm):
    """
    Form for creating a new Dojo.

    Attributes:
        name (StringField): Field to input the name of the Dojo.
        submit (SubmitField): Button to submit the form and create a new Dojo.
    """
    name = StringField("Name")
    submit = SubmitField("Create")

class NinjaForm(FlaskForm):
    """
    Form for creating a new Ninja.

    Attributes:
        dojo_id (SelectField): Dropdown to select the dojo for the Ninja. Populated by all existing dojos.
        first_name (StringField): Field to input the first name of the Ninja.
        last_name (StringField): Field to input the last name of the Ninja.
        age (IntegerField): Field to input the age of the Ninja.
        submit (SubmitField): Button to submit the form and create a new Ninja.
    """
    
    dojo_id = SelectField("Dojo", coerce=int)
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    age = IntegerField("Age", coerce=int)
    submit = SubmitField("Create")
