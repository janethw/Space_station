import sqlite3
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        # Establish a connection to the file pointed at by the DATABASE configuration key.
        # File gets created when the db is initialized later.
        print(f'{current_app.config['DATABASE_URI']=}')
        g.db = sqlite3.connect(
            # current_app is used as we are outside the application context.
            # It proxies the active application instance's configuration.
            current_app.config['DATABASE_URI'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        print(current_app.config['DATABASE_URI'])
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# init_db() and init_db_command() are Python functions to run the SQL commands in schema.sql
def init_db():
    db = get_db()
    try:
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
    except Exception as e:
        # Print exceptions
        print(e)
    # finally:
    #     db.commit()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


# init_app() takes an application and registers the close_db() and init_db_command() functions to it
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)