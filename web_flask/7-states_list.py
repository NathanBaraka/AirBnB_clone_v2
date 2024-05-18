#!/usr/bin/python3
"""
Starts a Flask web application that displays a HTML page with the states
listed in alphabetical order.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a HTML page with the states listed in alphabetical order.

    Returns:
        The rendered HTML template with the states list.
    """
    # Get all states from storage and sort them by name
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the storage on teardown.

    Args:
        exception: The exception that caused the teardown, if any.
    """
    storage.close()

if __name__ == '__main__':
    # Run the application on http://0.0.0.0:5000/
    app.run(host='0.0.0.0', port='5000')

