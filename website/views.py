'''
This is where the routes are defined.
It may be split into a package of its own (yourapp/views/) with
related views grouped together into modules.
'''
from flask import Blueprint
page = Blueprint('petes_meals', __name__)


@page.route('/')
def index():
    return "Index!"

@page.route("/hello")
def hello():
    return "Hello World!"

@page.route("/members")
def members():
    return "Members"

@page.route("/members/<string:name>/")
def getMember(name):
    return name