#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Displays 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ Displays 'C' followed by the text passed """
    return "C {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
