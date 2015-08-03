#!/usr/bin/env python
# coding=utf-8

from flask import Flask, jsonify, url_for, request
import json
app = Flask(__name__)

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
        print 'This is a POST'
        print data
        print request.values
        return 'Hello world!'
    if request.method == 'GET':
        print 'This is a GET'
        print request.values
        return 'Hello world!'     
     
@app.route('/translate_age', methods=['POST'])
def translate_age(): 
    print request.form
    answer=json.dumps({'id_status': 'Valid', 'birthdate': '1992-10-30'})
    print answer
    return answer
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)