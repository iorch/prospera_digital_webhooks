#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, jsonify, url_for, stream_with_context, request,
                   Response, make_response, current_app)
import requests
import os
import logging
from logging.handlers import RotatingFileHandler
import sys

sys.path.append(os.path.dirname(__file__))
from prospera_users import User, db
from datetime import timedelta
from functools import update_wrapper
import pandas as pd
import random
import beanstalkc
import json
import datetime

data_df = pd.read_csv('data.txt')

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
file_handler = RotatingFileHandler("./prosperapp.log", maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.DEBUG)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
db.init_app(app)

beanstalk_send = beanstalkc.Connection(host='127.0.0.1', port=11300)
beanstalk_send.use('whatsapp-send')

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


@app.route('/', methods=['POST', 'GET'])
@crossdomain(origin='*')
def index():
    resp = make_response('Hello world!')
    if request.method == 'POST':
        data = request.data
        if not data:
            data = request.form.keys()[0]
        return (resp)
    if request.method == 'GET':
        return resp


@app.route('/ping', methods=['GET'])
def ping():
    answer = json.dumps({'ping': 'pong'})
    return answer


@app.route('/translate_age', methods=['POST'])
def translate_age():
    user_form = request.form
    app.logger.debug(user_form)
    app.logger.debug(app.config['RAPIDPRO_TOKEN'])
    token = 'Token ' + app.config['RAPIDPRO_TOKEN']
    headers = {'Authorization': token}
    params = {'phone': user_form['phone']}
    app.logger.debug(params)
    r = requests.get('https://api.rapidpro.io/api/v1/contacts.json',
                     params=params, headers=headers)
    app.logger.debug(stream_with_context(r))
    answer = json.dumps({'id_status': 'Valid', 'birthdate': '1992-10-30'})
    return answer


@app.route('/query', methods=['GET'])
def query():
    prosperaId = int(request.args.get('prosperaId'))
    variables = request.args.getlist('variables')
    app.logger.debug(variables)
    user = User()
    query = user.query.filter_by(prosperaId=prosperaId).first()
    answer = {'prosperaId': prosperaId}
    for i in variables:
        answer[i] = getattr(query, i)
    app.logger.debug(json.dumps(answer, ensure_ascii=False).encode('utf8'))
    return json.dumps(answer, ensure_ascii=False).encode('utf8')


@app.route('/generate_random', methods=['GET'])
def genearte_random():
    random_range = range(1, int(request.args.get('random')) + 1)
    random_number = random.sample(random_range, 1)
    field = 'rp-random-1-' + str(request.args.get('random'))
    answer = {field: random_number}
    return json.dumps(answer, ensure_ascii=False).encode('utf8')


@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    false = False
    null = None
    phone = ''
    uuid = ''
    if request.method == 'GET':
        uuid = request.args.get('uuid')
        phone = request.args.get('pd2_phonenum')
    if request.method == 'POST':
        uuid = request.form['uuid']
        app.logger.debug(request.form)
        phone = request.form['pd2_phonenum']
    token = 'Token ' + str(app.config['RAPIDPRO_TOKEN'])
    app.logger.debug(phone)
    mydata = data_df[data_df['pd2_phoneNum'] == phone].to_dict('list')
    app.logger.debug(mydata)
    original_fields = ["id", "clues", "cluesForBirths", "cluesForBirths-jur",
                       "cluesForBirths-mun", "cluesForBirths-loc", "cluesForBirths-name",
                       "cluesForBirths-address", "clinicmeanTALLAH", "clinicmeanPESOH",
                       "movistar", "telcel3g", "telcelGsm", "rezagoSocial", "incidentesPerCapita",
                       "pd1-cluesName", "pd1-name", "pd1-nameF", "pd1-nameM", "pd1-birthDate",
                       "pd1-pregWeek", "pd1-highRisk", "pd1-prevPreg", "pd1-internalFolio",
                       "pd1-treatmentArm", "pd1-appts", "pd1-lastPregDate", "pd1-nextApptDate",
                       "pd1-nextWshpDate", "pd1-lastApptDate", "pd1-dueDate",
                       "pd1-age", "numdoctors", "numnurses", "ent-nombre",
                       "jur-clave", "jur-nombre", "mun-nombre", "loc-nombre",
                       "tipo-nombre", "domicilio", "cp", "clinicRezagoSocial",
                       "clinicPop6-11noa", "clinicPop8-14an", "clinicPop15sec-in",
                       "clinicPop15-an", "clinicPropVph-pisoti", "clinicPropVph-c-serv",
                       "clinicPropVph-refri", "clinicPropVph-cel", "clinicPropVph-inter",
                       "pd2-knowsPhone", "pd2-knowsPhoneYears", "pd2-benefit", "pd2-imei", "pd2-chip",
                       "pd2-phoneComp", "pd2-phoneNum", "pd3-isVocal", "pd3-isAux", "pd3-isVocalAux",
                       "pd3-numLocs", "pd3-assocLoc1", "pd3-assocLoc2", "pd3-assocLoc3",
                       "pd3-assocLoc4", "pd4-nutrivida", "pd4-consults", "pd4-messages"]
    valid_fields = map(lambda v: (v.lower().replace("-", "_")), original_fields)
    app.logger.debug(valid_fields)
    app.logger.debug(mydata.items())
    all_fields = dict(map(lambda (v, k): (str(k[0]).lower(), str(v[0])), mydata.iteritems()))
    app.logger.debug(all_fields)
    dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in y])
    app.logger.debug(dictfilt)
    fields = dictfilt(all_fields, valid_fields)
    headers = {'Authorization': token, 'content-type': 'application/json'}
    app.logger.debug(fields)
    params = {'uuid': uuid, 'fields': fields}
    r = requests.post('https://api.rapidpro.io/api/v1/contacts.json',
                      data=json.dumps(params, ensure_ascii=False).encode('utf8'), headers=headers)
    app.logger.debug(r.text)
    answer = json.dumps({'text': r.text,
                         'status_code': r.status_code})
    app.logger.debug(answer)

    return (answer, 200)

@app.route('/pdys', methods = ['POST'])
def pdys():
    data = request.args
    timestamp = str(datetime.datetime.utcnow())
    to_send = {"type": "simple",
                   "address": '521'+data['to']+'@s.whatsapp.net',
                   "body": data['text'],
                   "timestamp": timestamp}
    answer = json.dumps(request.args)
    message = json.dumps(to_send)
    beanstalk_send.put(message)
    #https://rapidpro.io/handlers/external/sent/b1435baa-abbd-4e8f-8b4a-3e252acefe52/
    return (answer, 200)

@app.route('/answer_rp', methods=['POST'])
def answer_rp():
    data = json.dumps(request.form,ensure_ascii=False).encode('utf8')
    app.logger.debug(data)
    r = requests.post('https://rapidpro.io/handlers/external/sent/b1435baa-abbd-4e8f-8b4a-3e252acefe52/',
                      data=data)
    answer = 'OK'
    return (answer, 200)



#@app.route('/whatsapp_received', methods = ['POST'])
#def whatsapp_received():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
