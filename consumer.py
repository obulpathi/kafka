from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

endpoint = "10.190.240.235:6667"
client = KafkaClient(endpoint)

print("After connecting to kafka")

consumer = SimpleConsumer(client, "group", "logs")

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
