from flask import Flask


def create_app():
    # Create new instance of the Flask class
    app = Flask(__name__)

    # Load the configuration

    # Set up the logging, connect the db, register blueprints/routes...

    # Return the fully set-up app
    return app
