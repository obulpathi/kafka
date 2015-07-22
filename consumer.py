from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

endpoint = "10.190.240.235:6667"
client = KafkaClient(endpoint)

print("After connecting to kafka")

consumer = SimpleConsumer(client, "group", "logs")

for message in consumer:
    print(message)
