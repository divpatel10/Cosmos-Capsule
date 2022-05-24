from nis import cat
from data.budget_parser.nasa_budget import *
from fastapi import APIRouter, Depends, Request

from models.Budget.Budget import Budget

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/budget",
    tags=["Budget"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def missions_base(req: Request):
    print(req.query_params)

    data = get_mission_list()
    return data

@router.get("/all")
async def mission_summary():
    data = get_mission_costs()    
    return data

@router.get("/{mission_name}")
async def mission(mission_name: str, req: Request):
    data = get_mission_detail(mission_name)
    return data

