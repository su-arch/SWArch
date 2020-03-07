 from flask import Flask, request, render_template
import os
import json
from flask.json import jsonify

@app.route('/api', methods-['GET'])
def api():
    return render_template('whatever html needed')

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.json #if posted using content type application/json then use request.get_json
    
    #pass data to validation module   TODO
    #receive a message
    
    message=""
    if message == "Success":
        return jsonify(data)
    else:
        return render_template('error.html', message = message), 400

@app.route('/api/query', methods=['POST'])
def query():
    queriedData = request.json
    
    #pass data for validation     TODO
    #receive message 
    
    message=""
    if message == "Success":
        return jsonify(queriedData)
    else:
        return render_template('error.html', message = message), 400

@app.route('/api/update/<addressID>', methods=['PUT'])
def update():
    updateData = request.json
    addressID = updateData['addressID']
    if addressID in checkAdressID: #a method in database to check if the adress id exists
    
        #send updateData for validation    TODO
        #store data in database    TODO
    
        return jsonify(updateData)
    else:
        return render_template("error.html", message="Address ID not found!!!!")
