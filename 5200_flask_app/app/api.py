from flask import Flask, request, render_template
import os
import json
from flask.json import jsonify
from app.validation import validate_upload, validate_update

@app.route('/api', methods-['GET'])
def api():
    return render_template('whatever html needed')

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    
    #pass data to validation module
    #receive a message
    message = validate_upload(data)
    #message=""
    if message == "Success":
        return jsonify(data)
    else:
        return render_template('error.html', message = message), 400

@app.route('/api/query', methods=['POST'])
def query():
    queriedData = request.get_json()
    #pass data for validation
    #receive message 
    message = validate_upload(queriedData)
    if message == "Success":
        return jsonify(queriedData)
    else:
        return render_template('error.html', message = message), 400

@app.route('/api/update/<addressID>', methods=['PUT'])
def update():
    updateData = request.get_json()
     #a method in database to check if the adress id exists
    validationMessage = validate_update(updateData)
    
    if validationMessage == "Success":
        return jsonify(updateData)
    else:
        return render_template("error.html", message=validationMessage)



