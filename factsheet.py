from fastapi import FastAPI, Query, Depends, Request
from pandas import DataFrame
from data.factsheet_parser import *
import json

from models.Planet import Planet

app = FastAPI()


@app.on_event("startup")
def startup():
    global scraped_data 
    scraped_data =  get_factsheet()
    

@app.get("/")
def home():
    return {"Data": "Endpoint Missing"}


@app.get("/factsheet", status_code=200)
async def factsheet(req: Request, params:Planet = Depends()):
    cur_data = scraped_data

    if req.query_params is not None:
        if req.query_params.get("units") is not None and req.query_params.get("units")  == IMPERIAL_DATA_TYPE:
            cur_data = get_factsheet(KEY_AS_PLANET,IMPERIAL_DATA_TYPE)
        
        if params.mass is not None :
            cur_data = scraped_data[scraped_data["Mass"] == params.mass]


    data = cur_data.to_json(orient='index')
    return json.loads(data)


