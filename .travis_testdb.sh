#!/usr/bin/env bash
mysql -e "create database IF NOT EXISTS user;" -uroot


mysql -u root -e "USE user; \
CREATE TABLE user (prosperaId bigint(20) NOT NULL, \
clues varchar(255) NOT NULL,  nom_mun varchar(255) NOT NULL);"


mysql -u root -e "USE user; \
INSERT INTO user VALUES \
(1511110987654321,\
'151111098',\
'GUADALAJARA');"

echo "USE mysql;\n
UPDATE user SET password=PASSWORD('$PRODIWEBHOOKS_MYSQL_ENV_MYSQL_ROOT_PASSWORD')
WHERE user='root';\n FLUSH PRIVILEGES;\n" | mysql -u root
