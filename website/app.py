'''
This file initializes your application and brings together all of the various components.
'''
from flask import Flask
from website import views, models, forms

def create_app():
    app_instance = Flask(__name__)
    app_instance.register_blueprint(views.page)
    app_instance.config.from_object('config')
    return app_instance


if __name__ == '__main__':
    app = create_app()
    app.config["LOG"].info('Starting environment')
    app.run(host='127.0.0.1')
