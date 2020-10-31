'''
This is where the routes are defined.
It may be split into a package of its own (yourapp/views/) with
related views grouped together into modules.
'''
from flask import Blueprint, render_template
from website.db import MongoDB
page = Blueprint('petes_meals', __name__)

'''
When connecting to the database, we are able to create multiple databases.
For public views, we are able to connect to a "public" facing database, whereas
for private/auth connections we can make sure we are only using the "private" facing
database that will only store admin creds.
'''


@page.route('/')
@page.route('/index')
def index():
    mongo = MongoDB("test").get_db()
    print(mongo)
    user = {"username": "Joe"}

    posts = [
        {
            'author': {'username': 'John'},
            'meal': 'Bronze Meal Plan'
        },
        {
            'author': {'username': 'Susan'},
            'meal': 'Silver Meal Plan'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@page.route("/hello")
def hello():
    return "Hello World!"

@page.route("/members")
def members():
    return "Members"

@page.route("/members/<string:name>/")
def getMember(name):
    return name
