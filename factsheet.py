from fastapi import FastAPI, Query
from data.factsheet_data import *
from typing import Optional
import json

from models.models import Planet

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Endpoint Missing"}

@app.get("/factsheet/")
async def factsheet(request: Planet = None, units=METRIC_DATA_TYPE):
    
    # if viewby == "property":
    #     data = get_factsheet(KEY_AS_PROPERTY)

    # else:

    if units == IMPERIAL_DATA_TYPE:
        data = get_factsheet(IMPERIAL_DATA_TYPE)
    else:
        data = get_factsheet()


    data = data.to_json(orient='index')
    return json.loads(data)


