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
async def missions_base():
    data = get_mission_list()
    return data
@router.get("/missions/{mission_name}")
async def mission(mission_name: str, req: Request):

    data = get_mission_detail(mission_name)
    return data

@router.get("/summary")
async def mission_summary(req: Request, params:Budget = Depends()):
    data = get_mission_costs()
    
    return data
