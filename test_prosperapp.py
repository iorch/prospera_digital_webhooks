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
        phone='+5211234567890'), follow_redirects=True)
    assert json.loads(response.data)['birthdate']=='1992-10-30'
    