from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class Lesson(BaseModel):
    id: Optional[int] = None
    title: str
    steps: list
    courses: List[int]
    units: List[int]

    model_config = ConfigDict(extra='ignore')
