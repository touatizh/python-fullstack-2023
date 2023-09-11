from enum import Enum
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Locations(Enum):
    """
    Enumeration representing different dojo locations.
    
    Attributes:
        Select: Placeholder prompting users to select a location.
        Tunis: Represents the dojo location in Tunis, TN.
        Bellevue: Represents the dojo location in Bellevue, WA.
        Silicon_Valley: Represents the dojo location in Silicon Valley, CA.
        Los_Angeles: Represents the dojo location in Los Angeles, CA.
    """
    Select = "---- Select a location ----"
    Tunis = "Tunis, TN"
    Bellevue = "Bellevue, WA"
    Silicon_Valley = "Silicon Valley, CA"
    Los_Angeles = "Los Angeles, CA"

class Languages(Enum):
    """
    Enumeration representing different programming languages.
    
    Attributes:
        Select: Placeholder prompting users to select a language.
        Python: Represents the Python programming language.
        Java: Represents the Java programming language.
        JS: Represents the JavaScript programming language.
        C_Sharp: Represents the C# programming language.
        DotNet: Represents the .NET framework.
    """
    Select = "---- Select a language ----"
    Python = "Python"
    Java = "Java"
    JS = "JavaScript"
    C_Sharp = "C#"
    DotNet = ".NET"

# Workaround to include "C#" and ".NET" as choices in the SelectField
lang_choices = [
    (Languages.Select, "---- Select a language ----"),
    (Languages.Python, "Python"),
    (Languages.Java, "Java"),
    (Languages.JS, "JavaScript"),
    (Languages.C_Sharp, "C#"),
    (Languages.DotNet, ".NET")
]

class SurveyForm(FlaskForm):
    """
    FlaskForm derived class representing the survey form.

    Attributes:
        name (StringField): Field to collect the user's name. It is a required field.
        location (SelectField): Dropdown field to select the dojo location. It is a required field.
        fav_lang (SelectField): Dropdown field to select the favorite programming language. It utilizes the lang_choices list to include "C#" and ".NET" as choices. 
        additional (TextAreaField): Text area field to collect additional information from the user.
        submit (SubmitField): Button to submit the form.
    """
    name = StringField(label="Name:", validators=[DataRequired()])
    location = SelectField(label="Dojo Location:", choices=[(loc.name, loc.value) for loc in Locations],
                           validators=[DataRequired()])
    fav_lang = SelectField(label="Favorite Language", choices=[(name.value, value) for name, value in lang_choices])
    additional = TextAreaField(label="Additional Information",  render_kw={"rows": 10, "cols": 11})
    submit = SubmitField("Submit")
