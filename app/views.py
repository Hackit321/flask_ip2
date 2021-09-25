from flask import render_template
from flask.templating import render_template_string
from app import app



@app.route('/')
def index():
    return render_template('index.html')



