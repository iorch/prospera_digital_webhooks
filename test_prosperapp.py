#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import prosperapp
import json
import random


@pytest.fixture
def app():
    return prosperapp.app


@pytest.fixture
def test_client(app):
    app.config.from_object('config.TestingConfig')
    return app.test_client()


def test_ping(test_client):
    response = test_client.get('/ping', follow_redirects=True)
    assert json.loads(response.data)['ping'] == 'pong'


def test_hello_get(test_client):
    response = test_client.get('/', )
    assert response.data.decode("utf-8") == 'Hello world!'


def test_hello_post(test_client):
    response = test_client.post('/', data=dict(
        title='test'), follow_redirects=True)
    assert response.data.decode("utf-8") == 'Hello world!'


def test_translate_age(test_client):
    response = test_client.post('/translate_age', data=dict(
        phone='(206) 555-0104'), follow_redirects=True)
    assert json.loads(response.data)['birthdate'] == '1992-10-30'


def test_query(test_client):
    response = test_client.get('/query?prosperaId=1511110987654321&variables=clues&variables=nom_mun', )
    assert json.loads(response.data.decode("utf-8"))['nom_mun'] == 'GUADALAJARA'

def test_generate_random_get(test_client):
    randomn=random.sample([4,6,8],1)[0]
    response = test_client.get('/generate_random?random={0}'.format(str(randomn)), )
    assert json.loads(response.data)["rp-random-1-{0}".format(str(randomn))][0] <= randomn

def test_get_info_post(test_client):
    response = test_client.post('/get_info', data=dict(
        uuid='c5c0814e-59e9-4327-95ec-073c0aa74936',
        prosperaId='1511110987654321',
        pd2_phonenum='(206) 555-0104'), follow_redirects=True)
    assert response.status == "200 OK"


def test_get_info(test_client):
    response = test_client.get('/get_info?uuid=c5c0814e-59e9-4327-95ec-073c0aa74936&pd2_phonenum=(206) 555-0104&prosperaId=1511110987654321', )
    assert response.status == "200 OK"

