from fastapi import APIRouter
from src import budget, factsheet

router = APIRouter()
router.include_router(factsheet.router)
router.include_router(budget.router)
