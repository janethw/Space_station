from flask import Flask, render_template, request, redirect, url_for
from space_station_backend.app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
