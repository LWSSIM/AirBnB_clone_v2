#!/usr/bin/python3
""" Starts a Flask web application """


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """ Display a HTML page with the states """
    states = storage.all(State)
    if id:
        key = "State." + id
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = states.values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
