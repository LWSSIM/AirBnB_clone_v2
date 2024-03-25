#!/usr/bin/python3
"""listen to a port and print the message received
connect to the database and fetch using session object
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list')
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """ Route function for /states and /states/<id> """
    not_found = False
    if id is not None:
        states = storage.all(State, id)
        _id = True
        if states is None:
            not_found = True
    else:
        states = storage.all(State)
        _id = False
    return render_template('9-states.html', states=states,
                           with_id=_id, not_found=not_found)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
