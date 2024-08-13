import logging
from logging.handlers import RotatingFileHandler


# Set up configuration for the root logger
logging.basicConfig(
    filename='app.log',  # sets the name of the file in which logs will be saved
    encoding='utf-8',
    filemode='a',  # 'a' means append
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
logging.debug("This will get logged")

# In Python, standard loggers are created and accessed using the getLogger function
# in the logging module.


# Instantiate a logger called 'name' that uses the RotatingFileHandler
def setup_logger(name):
    # Get logger specified by the name argument in __init__.py
    logger = logging.getLogger(name)

    # Add the handler if the logger doesn't already have one (to avoid duplicate entries)
    # Set log level to DEBUG
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        # Log to a file
        handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        logger.addHandler(handler)

    # return the configured logger is best practice
    return logger
