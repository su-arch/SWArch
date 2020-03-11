from flask import Flask, request, render_template
import os
import json
from flask.json import jsonify
from .validations import validate_upload, validate_update, validate_query
from . import app
from werkzeug.datastructures import ImmutableDict

@app.route('/api', methods=['GET'])
def api():
    return render_template('whatever html needed')

@app.route('/api/upload', methods=['POST'])
def api_upload():
    #validate_upload(data)
    #receive a message
    data = request.get_json(force=True)
    print('api side')
    print(data)
    result = validate_upload(data)
    return jsonify(result)

@app.route('/api/query', methods=['POST'])
def query():
    queriedData = request.get_json()
    #pass data for validation
    #receive message 
    result = validate_query(queriedData)
    return jsonify(result)


@app.route('/api/update/<addressID>', methods=['PUT'])
def update(addressID):
    updateData = request.get_json()
    result = validate_update(updateData, addressID)
    return jsonify(result)



