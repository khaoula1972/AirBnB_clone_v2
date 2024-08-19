#!/usr/bin/python3
"""
This module starts a simple Flask web application with three routes.
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

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns 'C ' followed by the value of the text variable, with underscores replaced by spaces.
    
    Args:
        text (str): The text to display after 'C '.
    
    Returns:
        str: A string that says 'C ' followed by the text with spaces instead of underscores.
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
