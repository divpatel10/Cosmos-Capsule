from fastapi import  Depends, Request, APIRouter
from data.factsheet_parser import *
from models.Planet import Planet
import json

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/factsheet",
    tags=["Factsheet"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
# Parameters - Request is the request body
#            - Planet Model
async def read_root(req: Request, params:Planet = Depends()):
    global scraped_data
    global scraped_data_us 
    scraped_data =  get_factsheet()
    scraped_data_us =  get_factsheet(IMPERIAL_DATA_TYPE)
    global cur_data
    cur_data = scraped_data

    print("All Query Params", (dict(req.query_params)))
    print("Planet Model Query Params",params )

    if req.query_params is not None:

       # Check for "units" Query
        if req.query_params.get("units") is not None \
             and req.query_params.get("units")  == IMPERIAL_DATA_TYPE:
            cur_data = scraped_data_us

        # Check for "planet" Query and filter the JSON response for the planet
        if req.query_params.get("planet") is not None:
            data = json.loads(cur_data.to_json(orient='index'))
            cur_planet = str(req.query_params.get("planet").upper()).replace("\"","")
            if cur_planet not in data:
                return {"Planet":"Not Found"}

            return data[cur_planet]
        
        else:
            # This list holds all the possible queries a user can make for a planet's property
            planet_properties = [v[0] for v in params]
            
            # iterate through all the queries if the user has made one
            for property in planet_properties:
                
                if req.query_params.get(property) is not None:
                    # Match the query with the dataframe
                    try:
                        col_name = [col for col in cur_data.columns if property.lower() in col.replace(" ","").lower()][0]
                    except:
                        return {"Error": "check /docs for the possible Queries that can be made"}
                    print("Foud Matching Column Name: ",col_name)
                    cur_data = cur_data[cur_data[col_name] == str(req.query_params.get(property))]
    data = cur_data.to_json(orient='index')
    return json.loads(data)


