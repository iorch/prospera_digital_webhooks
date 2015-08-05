#!/usr/bin/env python
# coding=utf-8

from flask import Flask, jsonify, url_for, stream_with_context, request, Response
import json
import requests
import os

#
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['POST','GET'])
def index(): 
    if request.method == 'POST':
        data = request.data # but data will be empty unless the request has the proper content-type header...
        if not data:
            data = request.form.keys()[0]
        return('Hello world!')
    if request.method == 'GET':
        return('Hello world!')     
     
@app.route('/translate_age', methods=['POST'])
def translate_age(): 
    user_form = request.form
    #print user_form
    print app.config['DEBUG']
    print app.config['RAPIDPRO_TOKEN']
    token = 'Token ' + app.config['RAPIDPRO_TOKEN']
    headers = {'Authorization': token}
    params = {'phone': user_form['phone']}
    r = requests.get('https://api.rapidpro.io/api/v1/contacts.json',
        params = params, headers = headers )
    print stream_with_context(r)
    answer=json.dumps({'id_status': 'Valid', 'birthdate': '1992-10-30'})
    return answer
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)