'''
This is where the routes are defined.
It may be split into a package of its own (yourapp/views/) with
related views grouped together into modules.
'''

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, sessions, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from website.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/auth/register', methods=('GET', 'POST'))
def register():
    return True


@auth.route('/auth/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}, remember me {form.remember_me.data}')
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)


# -------------------------
# Call backs

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view