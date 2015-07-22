import logging
from datetime import datetime

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer

logging.basicConfig()

endpoint = "172.17.0.5:9092"
client =  KafkaClient(endpoint)

producer = SimpleProducer(client)

msg = """This is message sent from python client fgskjfh fskdjfh skdjfkjs dfhksdf kjfskjdfsjkd kjfsjdkfsdfd
    sk kfjshkjdf jkjksfdfkjsd kjfsdhkjf sdhjkfsdkj ckjhdfk kjasfakfa kfakfhaskfasu kjfadkfj  aklfkasdf"""

for i in range(5000000):
    producer.send_messages("logs", msg)
