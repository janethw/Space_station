import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# Like the flaskr object, __name__ lets the bp know where it's defined
bp = Blueprint('auth', __name__, url_prefix='/auth')


# Register view function
# @bp.route decorator associates the URL/register with the register view function
# When Flask receives a request to /auth/register, it calls the register view and uses the return value as the response
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUE (?, ?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
            # A db IntegrityError will be raised if the username already exists
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                # url_for  generates the URL to a view based on the name and arguments.
                # The name associated with the view is called an endpoint
                # and, by default, is the same name as the view function and with the bp name prepended (if bp used)
                # Endpoint for the login function is 'auth.login'.
                return redirect(url_for("auth.login"))
        # flash() stores errors that can be retrieved when rendering the template
        flash(error)

    return render_template('auth/register.html')


# Login view function
# @bp.route decorator associates the URL/login with the login view function
# When Flask receives a request to /auth/login, it calls the login view and uses the return value as the response
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username)
        ).fetchone()

        if user is None or not check_password_hash(user['password'], password):
            error = 'Incorrect username or password.'

        if error is None:
            session.clear()
            # store user_id in the session dict cookie
            session['user_id'] = ['user_id']
            return redirect(url_for('index'))

        # flash() stores errors that can be retrieved when rendering the template
        flash(error)

    return render_template('auth/login.html')


# This function is registered with the bp and runs before the view function, no matter what URL is requested
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # Get user_id from db and store it on g.user, which lasts the length of the session
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
            ).fetchone()


# Remove user_id from session on logout
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# Require authentication in other views
# This decorator returns a new view function that wraps the original view it's applied to.
# If user is not loaded returns to login page, else original view is called and continues normally.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view