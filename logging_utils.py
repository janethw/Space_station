import logging
from logging.handlers import RotatingFileHandler

# LOGGING IN FLASK
# Use the app.logger object once the Flask app is set up

# HANDLERS
# The log handler sets out how a log is displayed or written.
# two key fields in log handler are: log formatter, which gives context information
# and the log level, which filters out logs of an inferior level.
# Console display with StreamHandler, write to a file with FileHandler

# TO DO: set up the logger for the Flask app


# In Python, standard loggers are created and accessed using the getLogger function
# in the logging module.
def setup_logger(name):
    # Get logger specified by the name argument in __init__.py
    logger = logging.getLogger(name)

    # Add the handler if the logger doesn't already have one (to avoid duplicate entries)
    # Set log level to INFO
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        # Log to a file
        handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        logger.addHandler(handler)

    # return the configured logger is best practice
    return logger
