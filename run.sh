#!/usr/bin/env/ bash

docker run -i -t \
--name prodiwebhooks_mysql \
-v data_prodi/mysql:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=$MY_MYSQL_ROOT_PASSWORD \
-p 3306:3306 -d mysql

docker run \
--name prodiwebhooks \
--link prodiwebhooks_mysql:prodiwebhooks_mysql \
-p 5001:5001 \
-e COVERALLS_REPO_TOKEN=$MY_COVERALL_TOKEN \
-e RAPIDPRO_TOKEN=$MY_RAPIDPRO_TOKEN \
prodiwebhooks
