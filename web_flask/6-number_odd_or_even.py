#!/usr/bin/python3
""" flask server """
from flask import Flask, render_template
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


@app.route('/python/<text>')
@app.route('/python/')
def python_text(text='is cool'):
    """ /python/<text> """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n=None):
    """ /number/<n> """
    return '{} is a number'.format(int(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """/number_template/<n> """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ /number_odd_or_even/<int:n> """
    if n % 2 == 0:
        x = 'even'
    else:
        x = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, x=x)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
