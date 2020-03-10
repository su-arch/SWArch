from flask import Flask, request, render_template
import os
import json
from flask.json import jsonify
from .validations import validate_upload, validate_update
from . import app
from werkzeug.datastructures import ImmutableDict

@app.route('/api', methods=['GET'])
def api():
    return render_template('whatever html needed')

@app.route('/api/upload', methods=['POST'])
def api_upload():
    data = request.form.to_dict()
    validate_upload(data)
    #receive a message
    message = validate_upload(data)
    #message=""
    if message == "Success":
        return jsonify(data)
    else:
        errorData = {"message": message,
                        "status": 400}
        return jsonify(errorData)

@app.route('/api/query', methods=['POST'])
def query():
    queriedData = request.form.to_dict()
    #pass data for validation
    #receive message 
    message = validate_upload(queriedData)
    if message == "Success":
        return jsonify(queriedData)
    else:
        errorData = {"message": message,
                        "status": 400}
        return jsonify(errorData)

@app.route('/api/update/<addressID>', methods=['PUT'])
def update():
    updateData = request.form.to_dict()
     #a method in database to check if the adress id exists
    validationMessage = validate_update(updateData)
    
    if validationMessage == "Success":
        return jsonify(updateData)
    else:
        errorData = {"message": validationMessage,
                        "status": 400}
        return jsonify(errorData)



