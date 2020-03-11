from flask import render_template, request, Response, jsonify
from . import app
from .forms import *
from .form_factory import *
from .db_functions import *
import requests

@app.route('/')
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    data = request.form.to_dict()
    print('data')
    print(data)
    if request.method == 'POST':
        response = requests.post('http://localhost:5000/api/upload', json=data)
        return(render_template('result.html', message=json.loads(response.content)))
    #POST the data to the /api/upload
    #get the JSON response from the API
    #render the results on the page
    return render_template('uploadpage.html')


@app.route('/query', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        data = request.form.to_dict()
        response = requests.post('http://localhost:5000/api/query', json=data)
        return(render_template('result.html', message=json.loads(response.content)))

    #get the JSON response from the API
    #if the response is error render error page
    #otherwise render the results on the page
    return render_template('downloadpage.html')

@app.route('/country_form')
def country_form():
    country = request.args.get('country_select', 0, type=str)

    print(country)
    form, fields = country_form_factory(country)
    if ('State' or 'Province' in fields) and country in RULE_VALID_PROVINCES.keys():
        opt_list = []
        print('State found ')
        state_dropdown_header = "<label class='dynamicForm' for='State'>State/Province</label><br> <select id='State'class='dynamicForm'>"
        for s in RULE_VALID_PROVINCES[country]:
            opt_html = "<option value='{}'>{}</option>".format(s,s)
            opt_list.append(opt_html)
        options = ''.join(opt_list)
        state_html = state_dropdown_header + options + '</select><br>'
        fields_html = ["<input name='{}' placeholder='{}' class='dynamicForm' type='text'><br>".format(field,field) for field in fields if field not in ['State', 'Province']]
        fields_html = [state_html] + fields_html
        return(jsonify(fields_html))

    fields_html = ["<input name='{}' placeholder='{}' class='dynamicForm' type='text'><br>".format(field,field) for field in fields]
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