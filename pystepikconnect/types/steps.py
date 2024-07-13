from pydantic import BaseModel
from typing import Optional


class Step(BaseModel):
    id: Optional[int] = None
    lesson: int
    position: int
    status: str
    block: dict

    class Config:
        extra = "ignore"
