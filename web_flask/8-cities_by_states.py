#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import *
from models import storage

# Create the Flask application
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display the states and cities listed in alphabetical order.

    Returns:
        The rendered HTML template '8-cities_by_states.html' with the states data.
    """
    # Retrieve all states from the storage
    states = storage.all("State").values()

    # Render the template with the states data
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.

    Args:
        exception: The exception that occurred during the request.
    """
    # Close the storage
    storage.close()


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port='5000')

