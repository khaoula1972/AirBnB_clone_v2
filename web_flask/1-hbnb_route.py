#!/usr/bin/python3
"""
This module starts a simple Flask web application with two routes.
"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns the string 'Hello HBNB!' when the root URL is accessed.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns the string 'HBNB' when the /hbnb URL is accessed.
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
