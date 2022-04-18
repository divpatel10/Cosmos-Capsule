from nis import cat
from data.nasa_budget import *
from fastapi import APIRouter, Depends, Request

from models.Budget.Budget import Budget

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/budget",
    tags=["Budget"],
    responses={404: {"description": "Not found"}},
)

@router.get("/summary")
async def mission(req: Request, params:Budget = Depends()):
    data = get_mission_costs()
    
    print(req.query_params)
    return data
