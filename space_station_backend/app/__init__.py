from flask import Flask
from config import DevelopmentConfig, TestingConfig
from logging_utils import setup_logger


def create_app():
    # Create new instance of the Flask class
    app = Flask(__name__)

    # Load the db development configuration (NB: the Flask object has a config attribute)
    app.config.from_object(DevelopmentConfig)

    # Load the Flask session secret key
    app.config.update(SECRET_KEY=DevelopmentConfig.SECRET_KEY)

    # Set up logging
    logger = setup_logger('app')

    # Connect the db, register blueprints/routes...

    # Return the fully set-up app
    return app
