import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import hvac
from confluent_kafka import Consumer, KafkaException
from pydantic import BaseModel
from predict import Predictor
from logger import Logger

logger = Logger(True)
log = logger.get_logger(__name__)
# log.info('Connecting to vault')
client = hvac.Client(
    url='http://vault:8200',
    token='testtoken',
)
log.info('Connected to vault')

read_response = client.secrets.kv.read_secret_version(path='my-secret-password')
log.info('Read secrets')
password = read_response['data']['data']['password']
# print(password)
log.info(password)

import psycopg2

conn =psycopg2.connect(
    dbname='penguinsDB',
    user='myuser1',
    password=password,
    host='db',
    port='5432'
)

cur = conn.cursor()



config = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(config)

class PinguinSchema(BaseModel):
    Culmen_Length: int 
    Culmen_Depth: int 
    Flipper_Length: int 
    Body_Mass: int 
    Delta15N: int 
    Delta13C: int 

consumer.subscribe(['penguin_topic'])
print('keka')
# try:
while True:
    # print('keka')
    msg = consumer.poll(timeout=0.1)
    # print(msg, ms)
    if msg is None:
        continue
    if msg.error():
        raise KafkaException(msg.error())
    else:
        # print(f'Received message: {msg.value().decode('utf-8')}')
        msg = msg.value().decode('utf-8')
        # print(type(msg))
        # msg_dict = json.loads(msg)
        # print(msg_dict, type(msg_dict))
        dec = PinguinSchema.model_validate_json(msg)
        print(dec, type(dec))
        predictor = Predictor()
        # tmp = 
        result = predictor.predict_api('SVM', dec)
        cur.execute(
            "INSERT INTO predict_results_test (result) VALUES (%s)",
            (result['data'],)
        )
        conn.commit()
        # return result
        
# except KeyboardInterrupt:
#     pass
# finally:
#     consumer.close()
