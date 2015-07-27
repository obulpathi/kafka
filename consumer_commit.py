from kafka import KafkaConsumer

# more advanced consumer -- multiple topics w/ auto commit offset
# management
consumer = KafkaConsumer('topic1', 'topic2',
                       bootstrap_servers=['localhost:9092'],
                       group_id='my_consumer_group',
                       auto_commit_enable=True,
                       auto_commit_interval_ms=30 * 1000,
                       auto_offset_reset='smallest')

# Infinite iteration
for m in consumer:
    # do_some_work(m)

    # Mark this message as fully consumed
    # so it can be included in the next commit
    #
    # **messages that are not marked w/ task_done currently do not commit!
    consumer.task_done(m)

    # If auto_commit_enable is False, remember to commit() periodically
    consumer.commit()

# Batch process interface
while True:
for m in kafka.fetch_messages():
    # process_message(m)
    consumer.task_done(m)
