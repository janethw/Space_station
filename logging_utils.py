import logging
from logging.handlers import RotatingFileHandler


# Set up configuration for the root logger
logging.basicConfig(
    # filename='app.log',  # sets the name of the file in which logs will be saved
    encoding='utf-8',  # ensures all input sources can be handled
    filemode='a',  # 'a' means append
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
logging.debug("This will get logged")

# In Python, standard loggers are created and accessed using the getLogger function
# in the logging module.


# Create a custom logger and set default level to DEBUG
def setup_logger(logger_name, level=logging.DEBUG):
    # Creates or retrieves an existing logger the name specified by logger_name
    logger = logging.getLogger(logger_name)

    # Check if logger is already configured
    if not logger.handlers:
        logger.setLevel(level)
        # Create a new file handler for the logger
        handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        logger.addHandler(handler)
        # Define the format of the logger messages
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Set the handler to use this format
        handler.setFormatter(formatter)

    # return the configured logger is best practice
    return logger
