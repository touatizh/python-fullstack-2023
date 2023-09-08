from flask import Flask, render_template, session, redirect, url_for, Response

# Create Flask app instance
app = Flask(__name__)

@app.route("/")
def index() -> str:
    """
    Handle requests to the home page.

    This function initializes a session counter to 1 and renders the index.html template.

    Returns:
        str: The rendered template as a string.
    """
    session["counter"] = session.get("counter", 0) + 1
    return render_template("index.html")

@app.route("/destroy_session")
def destroy_session() -> Response:
    """
    Clear visits counter and redirect to the home page.

    This function removes the "counter" from the session and then redirects the user to the home page.

    Returns:
        Response: A response object that redirects to the URL for the index function.
    """
    session.pop("counter", None)
    return redirect(url_for("index"))

@app.route("/plus_two")
def plus_two() -> str:
    """
    Increment the session counter by two.

    This function retrieves the current value of the "counter" from the session, increments it by two,
    and then renders the index.html template to reflect the updated counter value.

    Returns:
        str: The rendered template as a string.
    """
    session["counter"] = session.get("counter", 0) + 2
    return render_template("index.html", counter=session["counter"])

if __name__ == "__main__":
    # Secret key
    # ! secret key is hard coded on this assigement for the sake of simplicity only,
    # ! please keep your secret key safe and hidden on any production environment.
    app.secret_key = "C3nlQhWQiNkP9y_w8rPwIA"

    app.run(debug=True)