import json
import numpy as np
import time
from confluent_kafka import Producer
from pydantic import BaseModel
import time

config = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
}

producer = Producer(config)


class PinguinSchema(BaseModel):
    Culmen_Length: int 
    Culmen_Depth: int 
    Flipper_Length: int 
    Body_Mass: int 
    Delta15N: int 
    Delta13C: int 

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
    data = PinguinSchema(
        Culmen_Length = np.random.randint(0, 100), 
        Culmen_Depth = np.random.randint(0, 100), 
        Flipper_Length = np.random.randint(0, 100), 
        Body_Mass = np.random.randint(0, 100),
        Delta15N = np.random.randint(0, 100),
        Delta13C = np.random.randint(0, 100), 
    )
    send_message('penguin_topic', json.dumps(data.__dict__))
    time.sleep(1)