from app import app 
from urllib.request,json
import requests


api_key =None
s_url = None
art_url = None
articles_url =None


def configure_request(app):
    global api_key,s_url,art_url
    api_key = app.config['NEWS_API_KEY']
    articles_url =app.config['SOURCE_ARTICLE_URL']
    s_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['NEWS_ARTICLES_API_URL']

