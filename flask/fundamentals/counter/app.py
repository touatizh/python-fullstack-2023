from flask import Flask, render_template, session, redirect, url_for, Response, request

# Create Flask app instance
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """
    Handle requests to the home page.

    If the request method is GET, it increments the session counter by 1.
    If the request method is POST, it updates the session counter with the received "count" value from the JSON body of the request.
    
    The session counter is used to track the number of visits to the website.

    Returns:
        str: The rendered template as a string.
    """
    if request.method == "POST":
        count = request.get_json().get("count")
        if isinstance(count, int):
            session["counter"] = count
    else:
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
    Increment the session counter towards a total increment of two.

    This function obtains the current "counter" value from the session, increases it by one, and then 
    redirects to the index route where the counter is further incremented by one. 
    Consequently, the total increment in the counter through this route is two.

    Returns:
        Response: A Flask Response object resulting from redirecting to the index route.
    """
    session["counter"] = session.get("counter", 0) + 1
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Secret key
    # ! secret key is hard coded on this assigement for the sake of simplicity only,
    # ! please keep your secret key safe and hidden on any production environment.
    app.secret_key = "C3nlQhWQiNkP9y_w8rPwIA"

    app.run(debug=True)