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


if __name__ == "__main__":
    app.run()
