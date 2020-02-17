from . import app
from app.forms import *

@app.route('/')
@app.route('/index')
def index():
    return "Here is the top level index page for the webapp!"
