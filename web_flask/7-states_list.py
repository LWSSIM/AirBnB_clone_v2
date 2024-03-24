#!/usr/bin/python3
"""listen to a port and print the message received
connect to the database and fetch using session object
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_session(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
