#!/usr/bin/python3
"""Starts a simple flask webserver"""
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays n if it's a number using a template"""
    if isinstance(n, int):
        return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_html_even_odd(n):
    """Checks if n is odd or even"""
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run()
