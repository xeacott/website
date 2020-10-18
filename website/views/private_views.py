'''
This is where the routes are defined.
It may be split into a package of its own (yourapp/views/) with
related views grouped together into modules.
'''

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, sessions, url_for
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/auth/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        if not password:
            error = 'Password is required.'

    return True


@auth.route('/auth/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if username is None:
            error = 'Incorrect username.'

        flash(error)

    return render_template('auth/login.html')


# -------------------------
# Call backs

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view