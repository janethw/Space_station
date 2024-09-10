from logging_utils import setup_logger
from flaskr import create_app

# creates the Flask instance in the create_app function in __init__.py
app = create_app()

# Set up logger
logger = setup_logger(__name__)


if __name__ == "__main__":
    # Turning off the reloader stops Flask's built-in Werkzeug server,
    # which runs in debug mode by default, and so by default launches
    # the server twice: once for the actual server and once for reloader.
    # Turning off the reloader prevents the script from running twice.
    # app.run(debug=True, use_reloader=False)

    # However, for dev, we want the reloader to run, wo will leave it on,
    # even if it does mean some duplicate logs.
    app.run(debug=True)