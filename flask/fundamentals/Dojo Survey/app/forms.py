from flask_wtf import FlaskForm
from enum import Enum
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class Locations(Enum):
    Select = "---- Select a location ----"
    Tunis = "Tunis, TN"
    Bellevue = "Bellevue, WA"
    Silicon_Valley = "Silicon Valley, CA"
    Los_Angeles = "Los Angeles, CA"

class Languages(Enum):
    Select = "---- Select a language ----"
    Python = "Python"
    Java = "Java"
    JS = "JavaScript"
    C_Sharp = "C#"
    DotNet = ".NET"

class SurveyForm(FlaskForm):

    name = StringField(label="Name:", validators=[DataRequired()])
    location = SelectField(label="Dojo Location:", choices=[(loc.name, loc.value) for loc in Locations],
                           validators=[DataRequired()])
    fav_lang = SelectField(label="Favorite Language", choices=[(lang.name, lang.value) for lang in Languages])
    additional = TextAreaField(label="Additional Information",  render_kw={"rows": 10, "cols": 11})
    submit = SubmitField("Submit")