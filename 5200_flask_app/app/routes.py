from flask import render_template, request, Response, jsonify
from . import app
from .forms import *
from .form_factory import *
from .db_functions import *


@app.route('/')
@app.route('/upload')
def upload():
    #if request is POST
    #POST the data to the /api/upload
    #get the JSON response from the API
    #if the response is error render error page
    #otherwise render the results on the page
    return render_template('uploadpage.html')


@app.route('/query')
def download():
    #if request is POST
    #POST the data to the /api/query/route
    #get the JSON response from the API
    #if the response is error render error page
    #otherwise render the results on the page
    return render_template('downloadpage.html')

@app.route('/country_form')
def country_form():
    country = request.args.get('country_select', 0, type=str)
    print(country)
    form, fields = country_form_factory(country)
    fields.remove('submit')
    fields_html = ["<input name='{}' placeholder='{}' class='dynamicForm' type='text'><class='dynamicForm' br>".format(field,field) for field in fields]
    return jsonify(fields_html)
    #return render_template('bootstrap-example.html', form=form, fields=list(fields))


@app.route('/bootstrap')
def bootstrap_page():
    form, fields = country_form_factory('United States')
    print(vars(form))
    print(fields)
    return render_template('bootstrap-example.html', form=form, fields=list(fields))

'''
curl localhost:5000/test -d '{"id": "5e6688afd64550c9d16a36c6"}' -X POST -H "Content-Type: application/json"
curl localhost:5000/test -d '{"name": "CHILE"}' -X POST -H "Content-Type: application/json"
'''
# @app.route('/test', methods=['POST']) 
# def foo():
#     data = request.json
#     result = query_by_country_name(data['name'])
#     print (result)
#     return Response(response=str({'msg': 'successful'}), status=200, mimetype="application/json")