from confluent_kafka import Consumer, KafkaException

config = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(config)

consumer.subscribe(['test_topic'])
print('keka')
# try:
while True:
    print('keka')
    msg = consumer.poll(timeout=1.0)
    print(msg)
    if msg is None:
        continue
    if msg.error():
        raise KafkaException(msg.error())
    else:
        print(f'Received message: {msg.value().decode('utf-8')}')
# except KeyboardInterrupt:
#     pass
# finally:
#     consumer.close()
