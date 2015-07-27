from kafka import KafkaClient, MultiProcessConsumer

kafka = KafkaClient('localhost:9092')

# This will split the number of partitions among two processes
consumer = MultiProcessConsumer(kafka, b'my-group', b'my-topic', num_procs=2)

# This will spawn processes such that each handles 2 partitions max
consumer = MultiProcessConsumer(kafka, b'my-group', b'my-topic',
                                partitions_per_proc=2)

for message in consumer:
    print(message)

for message in consumer.get_messages(count=5, block=True, timeout=4):
    print(message)
