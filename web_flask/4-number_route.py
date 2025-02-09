#!/usr/bin/python3
"""
Starts a flask web application 4th task
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """
    Display hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Displays HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def c_with_params(text):
    """
    is_cool
    """
    text_no_underscore = text.replace("_", " ")
    return "C {}".format(text_no_underscore)


@app.route("/python", defaults={"text": "is_cool"})
@app.route("/python/<text>")
def python_txt_param(text):
    """
    display python text
    """
    text_no_underscore = text.replace("_", " ")
    return "Python {}".format(text_no_underscore)


@app.route("/number/<int:n>")
def number(n):
    """
    Display n as a number
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
