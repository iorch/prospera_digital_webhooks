from pystalkd.Beanstalkd import Connection
import datetime
import json
import requests
import os

beanstalks = Connection(host="127.0.0.1", port=int(11300))
beanstalkr = Connection(host="127.0.0.1", port=int(11300))
beanstalks.use('whatsapp-send')
beanstalkr.watch('whatsapp-receive')
job = None
message_received_url = os.environ.get('MESSAGE_RECEIVED_URL')

while (job==None):
    job = beanstalkr.reserve(timeout=1)
    if (job!=None):
        body = json.loads(job.body)
        job.delete()
        date = str(datetime.datetime.utcnow())
        address = str(body["address"]).split('@')[0]
        text = body["body"]
        to_send = {"from": address,
                   "text": "Mensaje: "+text+". Recibido a las "+str(body["timestamp"])+" desde el número: " + address,
                   "date": date}
        headers = {"Accept": "Application/json","Content-Type": "application/json"}
        r = requests.post(message_received_url,
                          data = json.dumps(to_send,ensure_ascii=False).encode('utf8'),headers=headers)
        to_send["to"] = str(body["address"])
        message = json.dumps(to_send)
        beanstalks.put(message)
        job = None
