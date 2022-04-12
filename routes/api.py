from fastapi import APIRouter
from src import factsheet

router = APIRouter()
router.include_router(factsheet.router)
