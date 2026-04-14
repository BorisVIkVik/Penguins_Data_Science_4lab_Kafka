import hvac
import sys
from dotenv import load_dotenv
import os

load_dotenv() 

DB_PSW = os.getenv('DB_PSW')

client = hvac.Client(
    url='http://vault:8200',
    token='testtoken',
)


create_response = client.secrets.kv.v2.create_or_update_secret(
    path='my-secret-password',
    secret=dict(password=DB_PSW),
)

print('Secret written successfully.')