import logging
from datetime import datetime

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer

batch_size = 50
batch_timeout = 60

logging.basicConfig()

endpoint = "10.190.240.235:6667"
client =  KafkaClient(endpoint)

producer = SimpleProducer(client, async=True,
                          batch_send_every_n=batch_size,
                          batch_send_every_t=batch_timeout)

producer = SimpleProducer(client, async=True,
    batch_send_every_n=batch_size, batch_send_every_t=batch_timeout)

msg = """This is message sent from python client fgskjfh fskdjfh skdjfkjs dfhksdf kjfskjdfsjkd kjfsjdkfsdfd
    sk kfjshkjdf jkjksfdfkjsd kjfsdhkjf sdhjkfsdkj ckjhdfk kjasfakfa kfakfhaskfasu kjfadkfj  aklfkasdf"""

print "Start time: " + str(datetime.now().time())
for i in range(5000000):
    producer.send_messages("logs", msg)
print "End time: " + str(datetime.now().time())
