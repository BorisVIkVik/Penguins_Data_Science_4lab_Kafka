import time
from confluent_kafka import Producer

config = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
}

producer = Producer(config)



def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivered failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_message(topic, message):
    producer.produce(topic, value=message, callback=delivery_report)
    producer.flush()        

while True:
    send_message('test_topic', f'Hello Kafka World! {time.time()}')