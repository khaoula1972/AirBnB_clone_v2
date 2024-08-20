#!/usr/bin/python3
"""
This module starts a simple Flask web application with five routes.
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

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Returns 'Python ' followed by the value of the text variable, with underscores replaced by spaces.
    
    Args:
        text (str): The text to display after 'Python '. Defaults to 'is cool'.
    
    Returns:
        str: A string that says 'Python ' followed by the text with spaces instead of underscores.
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns '<n> is a number' if n is an integer.
    
    Args:
        n (int): The integer to display.
    
    Returns:
        str: A string that says '<n> is a number' if n is an integer.
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

