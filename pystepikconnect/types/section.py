from pydantic import BaseModel
from typing import Optional


class Section(BaseModel):
    id: Optional[int] = None

    class Config:
        extra = "ignore"
