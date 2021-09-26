from flask import Flask
from config import config_option
from flask_bootstrap import Bootstrap


def create_app(config_name):
    app = Flask(__name__,)
    

    app.config.from_object(config_option[config_name])

    from .news_request import configure_request
    configure_request(app)


    return app 

