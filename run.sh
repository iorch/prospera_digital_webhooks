#!/usr/bin/env bash

docker run \
--name prodiwebhooks_mysql \
-e MYSQL_ROOT_PASSWORD=$MY_MYSQL_ROOT_PASSWORD \
-p 3306:3306 -d mysql

sleep 8
mysql -uroot -h 192.168.99.100 -proot < test.sql
mysql -uroot -h 192.168.99.100 -proot < messages.sql

docker run \
--name mxabierto-prospera_digital_webhooks \
--link prodiwebhooks_mysql:prodiwebhooks_mysql \
-e CELLPHONE=$MY_CELLPHONE \
-e TEST_PHONE=$TEST_PHONE \
-e PASSWORD=$MY_WHATSAPP_PASSWORD \
-p 11300:11300 \
-p 5001:5001 \
-e COVERALLS_REPO_TOKEN=$MY_COVERALLS_TOKEN \
-e RAPIDPRO_TOKEN=$MY_RAPIDPRO_TOKEN \
-e MESSAGE_RECEIVED_URL=$MY_MESSAGE_RECEIVED_URL \
-e PD2_PHONENUM="$PD2_PHONENUM" \
-e UUID=$MYUUID \
mxabierto-prospera_digital_webhooks
