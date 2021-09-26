from flask import Flask
from config import config_option


def create_app(config_name):
    app = Flask(__name__,)
