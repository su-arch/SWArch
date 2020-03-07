from flask import render_template
from . import app
from .forms import *


@app.route('/')
@app.route('/index')
def index():
    return "Here is the top level index page for the webapp!"

@app.route('/bootstrap')
def bootstrap_page():
    return render_template('bootstrap-example.html')
