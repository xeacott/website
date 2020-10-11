'''
This file initializes your application and brings together all of the various components.
'''
from flask import Flask
from website import views, models, forms

app = Flask(__name__)
app.register_blueprint(views.page)
app.config.from_object('config')


if __name__ == '__main__':
    app.config["LOG"].info('Starting environment')
    app.run(host='127.0.0.1')
