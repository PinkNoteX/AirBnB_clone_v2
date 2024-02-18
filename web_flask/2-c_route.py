#!/usr/bin/python3
""" flask server """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """ hello flask """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ /c/<text> """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
