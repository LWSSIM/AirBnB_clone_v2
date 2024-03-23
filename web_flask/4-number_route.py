#!/usr/bin/python3
"""starts a Flask web application that listens on 0.0.0.0:5000
 The routes:
   /: display "Hello HBNB!
   /hbnb: "HBNB"
   /c/<text>: display “C ” followed by the value of the text variable
   (replace underscore _ symbols with a space )
   /python/<text>: displat "Python", followed by text var,
   (text defaults to "is cool")
   /number/<n>: display “n is a number” only if n is an integer
 You must use the option strict_slashes=False in your route definition
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
