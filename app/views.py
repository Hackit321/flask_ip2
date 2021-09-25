from flask import render_template
from flask import render_templ
from app import app



@app.route('/')
def index():
    return render_template('index.html')



