from .forms import SurveyForm
from flask import request, render_template, session, redirect, url_for

def index():
    """
    View function to render the home page with the survey form.
    
    It initializes a SurveyForm instance and passes it to the 'index.html' template.
    
    Returns:
        render_template: Renders and returns the 'index.html' template with the SurveyForm instance.
    """
    form = SurveyForm()
    return render_template("index.html", form=form)

def process():
    """
    View function to handle form submission and store data in the session.
    
    It retrieves the form data from the POST request and stores it in the Flask session.
    Then, it redirects the user to the 'result' view function to display the survey results.
    
    Returns:
        redirect: Redirects the user to the 'result' view function.
    """
    session["name"] = request.form.get("name")
    session["location"] = request.form.get("location")
    session["fav_lang"] = request.form.get("fav_lang")
    session["additional"] = request.form.get("additional")

    return redirect(url_for("dojo_survey.result"))

def result():
    """
    View function to display the survey results.
    
    It retrieves the survey data stored in the session and creates a dictionary to organize the data.
    Then, it passes the data to the 'result.html' template to display the survey results.
    
    Returns:
        render_template: Renders and returns the 'result.html' template with the survey data.
    """
    survey_info = {
        "Name": session.get("name"),
        "Location": session.get("location"),
        "Favorite Language": session.get("fav_lang"),
        "Additional Information": session.get("additional")
    }
    return render_template("result.html", data=survey_info)
