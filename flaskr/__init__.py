import os

from flask import Flask
from instance.config import DevelopmentConfig
from logging_utils import setup_logger


# create_app is the application factory function
def create_app(test_config=None):
    # Create new instance of the Flask class
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config is passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    # # Set up logging
    # logger = setup_logger('app')
    #
    # # Test log
    # logger.info('App started')

    # Connect the db, register blueprints/routes...

    # Return the fully set-up app
    return app
