#!/usr/bin/python3
"""
This module starts a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns the string 'Hello HBNB!' when the root URL is accessed.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    # Start the Flask application listening on all available IP addresses on port 5000
    app.run(host="0.0.0.0", port=5000)
