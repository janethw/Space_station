import logging


# LOGGING IN FLASK
# Use the app.logger object once the Flask app is set up

# HANDLERS
# The log handler sets out how a log is displayed or written.
# two key fields in log handler are: log formatter, which gives context information
# and the log level, which filters out logs of an inferior level.
# Console display with StreamHandler, write to a file with FileHandler

# TO DO: set up the logger for the Flask app


def setup_logger(name):
    # Get logger specified by the name argument in __init__.py
    logger = logging.getLogger(name)

    # Configure Flask logging
    # Set log level to INFO
    logger.setLevel(logging.INFO)
    # Log to a file
    handler = logging.FileHandler('app.log')
    logger.addHandler(handler)