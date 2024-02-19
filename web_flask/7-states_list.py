#!/usr/bin/python3
""" flask server """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_lists():
    """ states_lists """
    s_dict = storage.all('State')
    s_list = []

    for state in s_dict.values():
        s_list.append(state)
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def closer(e):
    """ closer """
    storage.clsoe()


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
