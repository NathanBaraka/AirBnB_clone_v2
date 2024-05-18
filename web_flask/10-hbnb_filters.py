#!/usr/bin/python3
"""
Starts a Flask web application that displays a HTML page with the HBNB filters.
"""

from flask import Flask, render_template
from models import *
from models import storage


# Create the Flask application
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Display a HTML page with the HBNB filters.

    Returns:
        The rendered HTML template '10-hbnb_filters.html' with the states and
        amenities data.
    """
    # Get all states from storage
    states = storage.all("State").values()

    # Get all amenities from storage
    amenities = storage.all("Amenity").values()

    # Render the template with the states and amenities data
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the storage on teardown.

    Args:
        exception: The exception that caused the teardown, if any.
    """
    # Close the storage
    storage.close()


if __name__ == '__main__':
    # Run the Flask application on http://0.0.0.0:5000/
    app.run(host='0.0.0.0', port='5000')
