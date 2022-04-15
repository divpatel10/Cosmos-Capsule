from nis import cat
from data.nasa_budget import *
from fastapi import APIRouter


#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/budget",
    tags=["Budget"],
    responses={404: {"description": "Not found"}},
)

@router.get("/mission")
async def mission():
    data = get_mission_costs()
    return data
    
