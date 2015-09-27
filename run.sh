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
prospera_digital

prodiwebhooks_mysql:
  image: mysql
  ports:
    - "3306"
  volumes:
    - /prospera_digital/data:/var/lib/mysql
  environment:
    - MYSQL_ROOT_PASSWORD=helloNSA
prodiwebhooks:
  image: tutum.co/i0rch/prospera_digital_webhooks
  links:
      - prodiwebhooks_mysql
    ports:
      - "5001:5001"
    environment:
      - RAPIDPRO_TOKEN=bae15e0a8572ddb5f0e1c1fb8bb3733c84e3a746
      - COVERALLS_REPO_TOKEN=bXnLtdX1UKRgQOMw9lXWJDgM9Sp7wRWoS
