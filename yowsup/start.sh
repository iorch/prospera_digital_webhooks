#!/usr/bin/env bash
cd /yowsup-queue


cat config.sample.ini | \
sed "s/1234567/$CELLPHONE/g;s/<password in base64-format>/$PASSWORD/g" > config.ini

beanstalkd -l 127.0.0.1 -p 11300 &

python3 run.py &

sleep 5

ps aux| grep python3 | awk '{print $2}'|xargs kill -9

python3 run.py > /log.log &

cd /root/prospera_digital_webhooks/yowsup
python3 beanstalk-pd.py > messages.log
