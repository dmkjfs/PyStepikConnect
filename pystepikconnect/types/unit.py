from pydantic import BaseModel, ConfigDict
from typing import Optional


class Unit(BaseModel):
    id: Optional[int] = None
    section: int
    lesson: int

    model_config = ConfigDict(extra='ignore')
