#!/usr/bin/python3
"""Starts a simple flask webserver"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """Displays the text below on the browser"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()