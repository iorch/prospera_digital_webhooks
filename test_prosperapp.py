#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import prosperapp
import json

@pytest.fixture
def app():
    return prosperapp.app

@pytest.fixture
def test_client(app):
    app.config.from_object('config.TestingConfig')
    return app.test_client()

def test_hello_get(test_client):
    response = test_client.get('/',)
    assert response.data.decode("utf-8")=='Hello world!'

def test_hello_post(test_client):
    response = test_client.post('/',data=dict(
        title='test'), follow_redirects=True)
    assert response.data.decode("utf-8")=='Hello world!'

def test_translate_age(test_client):
    response = test_client.post('/translate_age',data=dict(
        phone='(206) 555-0104'), follow_redirects=True)
    assert json.loads(response.data)['birthdate']=='1992-10-30'

def test_query(test_client):
    response = test_client.get('/query?prosperaId=1511110987654321&variables=clues&variables=nom_mun',)
    assert json.loads(response.data.decode("utf-8"))['nom_mun']=='GUADALAJARA'
