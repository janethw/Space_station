from flask import Flask, render_template, request, redirect, url_for
# In from logging_utils import init_logger
from space_station_backend.app import create_app

# creates the Flask instance in the create_app function in __init__.py
app = create_app()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
