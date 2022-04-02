from fastapi import FastAPI, Query, Depends, Request
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
    print(params)
    cur_data = scraped_data
    if req.query_params["units"] == IMPERIAL_DATA_TYPE:
        cur_data = get_factsheet(IMPERIAL_DATA_TYPE)
    
    data = cur_data.to_json(orient='index')
    return json.loads(data)


