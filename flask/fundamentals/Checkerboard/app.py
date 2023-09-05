from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the default checkerboard.

    This function renders an 8x8 checkerboard.

    Returns:
        str: Rendered HTML template for an 8x8 checkerboard.
    """
    dimensions = {
        "height": 8,
        "width": 8
    }
    return render_template("index.html", dimensions=dimensions)

@app.route("/<x>")
def x_by_eight(x: str) -> str:
    """
    Renders a checkerboard of given height and default width of 8.

    Args:
        x (str): Height of the checkerboard.

    Returns:
        str: Rendered HTML template for the checkerboard of size x by 8.
    """
    dimensions = {
        "height": int(x),
        "width": 8
    }
    return render_template("index.html", dimensions=dimensions)

@app.route("/<x>/<y>")
def x_by_y(x: str, y: str) -> str:
    """
    Renders a checkerboard of given height and width.

    Args:
        x (str): Height of the checkerboard.
        y (str): Width of the checkerboard.

    Returns:
        str: Rendered HTML template for the checkerboard of size x by y.
    """
    dimensions = {
        "height": int(x),
        "width": int(y)
    }
    return render_template("index.html", dimensions=dimensions)

@app.route("/<x>/<y>/<color1>/<color2>")
def x_by_y_colors(x: str, y: str, color1: str, color2: str) -> str:
    """
    Renders a checkerboard of given size with specified colors.

    Args:
        x (str): Height of the checkerboard.
        y (str): Width of the checkerboard.
        color1 (str): Color for the even cells.
        color2 (str): Color for the odd cells.

    Returns:
        str: Rendered HTML template for the checkerboard with the given colors.
    """
    dimensions = {
        "height": int(x),
        "width": int(y),
    }
    colors = {
        "color1": color1,
        "color2": color2
    }
    return render_template("index.html", dimensions=dimensions, colors=colors)

if __name__ == "__main__":
    app.run(debug=True)
