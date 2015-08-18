#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, jsonify, url_for, stream_with_context, request,
    Response, make_response)
import json
import requests
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import timedelta
import sys
sys.path.append(os.path.dirname(__file__))
from prospera_users import User,db

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
file_handler = RotatingFileHandler("./prosperapp.log", maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.DEBUG)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
db.init_app(app)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/', methods=['POST','GET'])
def index():
    resp = make_response('Hello world!')
    if request.method == 'POST':
        data = request.data 
        if not data:
            data = request.form.keys()[0]
        return(resp)
    if request.method == 'GET':
        return(resp)

@app.route('/translate_age', methods=['POST'])
def translate_age():
    user_form = request.form
    #print user_form
    app.logger.debug(app.config['DEBUG'])
    app.logger.debug(app.config['RAPIDPRO_TOKEN'])
    token = 'Token ' + app.config['RAPIDPRO_TOKEN']
    headers = {'Authorization': token}
    params = {'phone': user_form['phone']}
    r = requests.get('https://api.rapidpro.io/api/v1/contacts.json',
        params = params, headers = headers )
    app.logger.debug(stream_with_context(r))
    answer=json.dumps({'id_status': 'Valid', 'birthdate': '1992-10-30'})
    return answer

@app.route('/query', methods=['GET'])
def query():
    uuid = request.args.get('uuid')
    variables = request.args.getlist('variables')
    app.logger.debug(variables)
    user = User()
    query = user.query.filter_by(dependenciaId=uuid).first()
    answer = { 'uuid': uuid}
    for i in variables:
        answer[i] = getattr(query,i)
    app.logger.debug(json.dumps(answer, ensure_ascii=False).encode('utf8'))
    return json.dumps(answer, ensure_ascii=False).encode('utf8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
