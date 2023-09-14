from .forms import UserForm
from flask import request, render_template, redirect, url_for
from .models import User

def index():
    """
    Fetch and display a list of all users.

    This function retrieves all users from the database using the User.get_all class method and then renders an HTML template to display the list of users in a table.

    Returns:
        str: The rendered HTML template as a string.
    """
    users = User.get_all()

    return render_template("index.html", users=users)

def add_new_user():
    """
    Handle the addition of a new user through a form.

    If the request method is POST, this function retrieves the form data, removes unnecessary fields, and saves the remaining data as a new user in the database using the User.save class method. It then redirects to the index view.

    If the request method is not POST, it simply renders an HTML template to display the form for adding a new user.

    Returns:
        str or Response: The rendered HTML template as a string (for GET requests) or a Response object to redirect to the index view (for POST requests).
    """
    
    if request.method == "POST":
        form = UserForm(request.form)
        
        data = {field[0]: field[1] for field in form.data.items() if field[0] != "submit" and field[0] != "csrf_token"}
        User.save(data)
        return redirect(url_for("user_cr.index"))
    
    form = UserForm()
    
    return render_template("add_user.html", form=form)
