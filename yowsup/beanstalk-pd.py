from pystalkd.Beanstalkd import Connection
import datetime
import json
import requests

#beanstalks = Connection(host="127.0.0.1", port=int(11300))
beanstalkr = Connection(host="127.0.0.1", port=int(11300))
#beanstalks.use('whatsapp-send')
beanstalkr.watch('whatsapp-receive')
job = None
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
                   "date": timestamp}
        message = json.dumps(to_send)
        r = requests.post("http://localhost:5001/answer_rp",
                          data = json.dumps(to_send,ensure_ascii=False).encode('utf8'))
        #beanstalks.put(message)
        job = None
