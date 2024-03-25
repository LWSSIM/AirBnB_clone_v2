#!/usr/bin/python3
"""listen to a port and load all cities of a state
with teardown function
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           states=states)


@app.teardown_appcontext
def teardown_session(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
