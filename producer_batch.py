import logging
from datetime import datetime

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer

batch_size = 50
batch_timeout = 60

logging.basicConfig()

endpoint = "10.190.240.235:6667"
client =  KafkaClient(endpoint)

producer = SimpleProducer(client, async=False,
    batch_send_every_n=batch_size, batch_send_every_t=batch_timeout)

msg = """This is message sent from python client fgskjfh fskdjfh skdjfkjs dfhksdf kjfskjdfsjkd kjfsjdkfsdfd
    sk kfjshkjdf jkjksfdfkjsd kjfsdhkjf sdhjkfsdkj ckjhdfk kjasfakfa kfakfhaskfasu kjfadkfj  aklfkasdf"""

batched_msg = (msg + "\n") * 50
print "Start time: " + str(datetime.now().time())
for i in range(100000):
    producer.send_messages("logs", batched_msg)
print "End time: " + str(datetime.now().time())
