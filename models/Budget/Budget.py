from typing import Optional
from pydantic import BaseModel

class Budget(BaseModel):
    developmentlaunch: Optional[str] = None
    operations: Optional[str] = None
    total: Optional[str] = None
    timeline: Optional[dict] = None