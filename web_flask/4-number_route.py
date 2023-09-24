#!/usr/bin/python3
"""Starts a simple flask webserver"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays the text below on the browser"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the text below on the browser"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Displays c followed with text stored in text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Displays Python followed with text stored in text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays n if it's a number"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
