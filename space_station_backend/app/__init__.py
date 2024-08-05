from flask import Flask
from config import DevelopmentConfig, TestingConfig


def create_app():
    # Create new instance of the Flask class
    app = Flask(__name__)

    # # Load the db configuration (NB: the Flask object has a config attribute)
    # app.config.from_object(DevelopmentConfig)
    #
    # # Load the Flask session secret key
    # app.config.update(DevelopmentConfig.SECRET_KEY)

    # Set up the logging, connect the db, register blueprints/routes...

    # Return the fully set-up app
    return app
