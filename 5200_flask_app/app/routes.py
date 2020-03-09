from flask import render_template, request, Response
from . import app
#from .forms import *
from .db_functions import *


@app.route('/')
@app.route('/index')
def index():
    return "Here is the top level index page for the webapp!"

@app.route('/bootstrap')
def bootstrap_page():
    return render_template('bootstrap-example.html')

'''
curl localhost:5000/creat -d '{"name":"test", "age":10}' -X POST -H "Content-Type: application/json"
'''
# @app.route('/creat', methods=['POST']) 
# def foo():
#     data = request.json
#     update(data)
#     return Response(response=str({'msg': 'successful'}), status=200, mimetype="application/json")

