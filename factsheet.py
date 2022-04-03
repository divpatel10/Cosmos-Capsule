from fastapi import FastAPI, Query, Depends, Request
from pandas import DataFrame
from data.factsheet_parser import *
import json

from models.Planet import Planet

app = FastAPI()


@app.on_event("startup")
def startup():
    global scraped_data
    global scraped_data_us 
    scraped_data =  get_factsheet()
    scraped_data_us =  get_factsheet(KEY_AS_PLANET,IMPERIAL_DATA_TYPE)
    

@app.get("/")
def home():
    return {"Data": "Endpoint Missing"}

@app.get("/factsheet", status_code=200)

async def factsheet(req: Request, params:Planet = Depends()):
    cur_data = scraped_data

    print("All Query Params",req.query_params)
    print("Planet Model Query Params",params )

    if req.query_params is not None:
       
        if req.query_params.get("units") is not None \
             and req.query_params.get("units")  == IMPERIAL_DATA_TYPE:

            cur_data = scraped_data_us

        planet_properties = [v[0] for v in params]
        for property in planet_properties:

            if req.query_params.get(property) is not None:
                col_name = [col for col in scraped_data.columns if property.lower() in col.replace(" ","").lower()][0]
                cur_data = scraped_data[scraped_data[col_name] == str(req.query_params.get(property))]
                print("Foud Matching Column Name: ",col_name)

    data = cur_data.to_json(orient='index')
    return json.loads(data)


