from flask import render_template
from flask import render_template,request,redirect,
from app import app



@app.route('/')
def homepage():
    '''
    views that renders new source to the homepage
    '''
    newsapi = NewsApiClient(NEWS_API_KEY = 'f4de1ca5f663456ea8bae142093fb813')
   



