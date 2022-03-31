from fastapi import FastAPI
from factsheet_data import *
import json

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Endpoint Missing"}

@app.get("/metric")
def metric():
    return json.loads(get_factsheet(METRIC_DATA_TYPE))

@app.get("/us")
def metric():
    return json.loads(get_factsheet(IMPERIAL_DATA_TYPE))

