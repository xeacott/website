''' index file for REST APIs using FLask'''

import os
import sys
import os
import json
import datetime
from modules.logger import logger
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

# Create a logger object to log the info and debug
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

# Create a logger object to log the info and debug
LOG = logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'output.log'))

# Setup environment stuff
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

# Port variable to run the server on.
PORT = os.environ.get('PORT')


@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == '__main__':
    LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development'
    app.run(host='127.0.0.1') # Run the app