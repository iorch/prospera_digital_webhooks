#!/bin/bash
export locale-gen en_US.UTF-8
export LANG=en_US.UTF-8
export LANG=C.UTF-8

cd /root/prospera_digital_webhooks
mkdir ../logs
pip install -r requirements.txt

py.test --cov=prosperapp.py
COVERALLS_REPO_TOKEN=$COVERALLS_REPO_TOKEN coveralls

python prosperapp.py