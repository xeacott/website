'''
This file initializes your application and brings together all of the various components.
'''

# Standard Imports
# none

# 3rd Party Imports
from flask import Flask

# Relative Imports
from website.views import public_views


class Website(Flask, object):
    '''
    Class to store main flask and mongo instance.
    '''
    def __init__(self, parent=None):
        super(Website, self).__init__(__name__, parent)
        self.website = None
        self.db = None
        self.create_app()

    def create_app(self):
        '''
        Create instance of application.
        '''
        app = Flask(__name__)
        app.config.from_object('config')
        app.config.from_pyfile('instance_config.py')
        self.website = app

    def init(self):
        '''
        Create the environment for the website to operate inside of.
        '''
        self.website.register_blueprint(public_views.page)

        self.run()

    def run(self):
        self.website.config["LOG"].info("Starting environment")
        self.website.run(host="127.0.0.1")
