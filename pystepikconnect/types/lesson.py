from pydantic import BaseModel
from typing import Optional, List


class Lesson(BaseModel):
    id: Optional[int] = None
    title: str
    steps: list
    courses: List[int]
    units: List[int]

    class Config:
        extra = "ignore"
