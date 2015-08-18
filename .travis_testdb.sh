#!/usr/bin/env bash
mysql -e "create database IF NOT EXISTS dependencia;" -uroot


mysql -u root -e "USE dependencia; \
CREATE TABLE dependencia (dependenciaId bigint(20) NOT NULL, \
ambito_id bigint(20) DEFAULT NULL,  articulo_id bigint(20) DEFAULT NULL,  \
descdependencia varchar(255) NOT NULL,  nomDependencia varchar(255) NOT NULL);"


mysql -u root -e "USE dependencia; \
INSERT INTO dependencia VALUES \
(10,3,1,\
'Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado',\
'ISSSTE');"

echo "USE mysql;\n
UPDATE user SET password=PASSWORD('$PRODIWEBHOOKS_MYSQL_ENV_MYSQL_ROOT_PASSWORD')
WHERE user='root';\n FLUSH PRIVILEGES;\n" | mysql -u root
