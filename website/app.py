'''
This file initializes your application and brings together all of the various components.
'''
from flask import Flask
from website import views, models, forms
from flask_pymongo import PyMongo


class Website(Flask):
    '''
    Class to store main flask and mongo instance.
    '''
    def __init__(self):
        super(Website, self).__init__(__name__)
        self.website = None
        self.mongo = None
        self.create_app()

    def create_app(self):
        '''
        Create instance of application and mongo.
        '''
        app = Flask(__name__)
        app.register_blueprint(views.page)
        app.config.from_object('config')
        app.config.from_pyfile('instance_config.py')
        mongo = PyMongo(app)

        # Instance assignments
        self.website = app
        self.mongo = mongo


if __name__ == '__main__':
    app = Website().website
    app.config["LOG"].info('Starting environment')
    app.run(host='127.0.0.1')
