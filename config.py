'''
This file contains most of the configuration variables that your app needs.
'''
import sys
import os
from website.logger import logger

# Create a logger object to log the info and debug
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'static'))

# Create a logger object to log the info and debug
LOG = logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, '../output.log'))

# Port variable to run the server on.
PORT = os.environ.get('PORT')

# Available as app.config["DEBUG"] for example
DEBUG = False  # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12  # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "eacott.joe@gmail.com"  # For use in application emails
