import uuid
import hvac
from fastapi import FastAPI, Body, status, Form
from fastapi.responses import JSONResponse, FileResponse
from test_predict import Predictor
from test_logger import Logger
from pydantic import BaseModel
from typing import Annotated
class PinguinSchema(BaseModel):
    Culmen_Length: int 
    Culmen_Depth: int 
    Flipper_Length: int 
    Body_Mass: int 
    Delta15N: int 
    Delta13C: int 
 

# config = configparser.ConfigParser()
logger = Logger(True)
log = logger.get_logger(__name__)

client = hvac.Client(
    url='http://vault:8200',
    token='testtoken',
)


read_response = client.secrets.kv.read_secret_version(path='my-secret-password')

password = read_response['data']['data']['password']
# print(password)
log.info(password)

import psycopg2

conn =psycopg2.connect(
    dbname='penguinsDB',
    user='myuser',
    password=password,
    host='db',
    port='5432'
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS predict_results_test (
        id SERIAL PRIMARY KEY,
        result VARCHAR(50)
    );
""")
conn.commit()
 
app = FastAPI()
 
@app.get("/")
async def main():
    return FileResponse("public/index.html")
 
 
@app.post("/api/predict")
def get_person(model, pinguin: Annotated[PinguinSchema, Form()]):
    predictor = Predictor()
    # tmp = 
    result = predictor.predict_api(model,pinguin)
    cur.execute(
        "INSERT INTO predict_results_test (result) VALUES (%s)",
        (result['data'],)
    )
    conn.commit()
    return result
