from pydantic import BaseModel
from typing import Optional
from pystepikconnect.types.block import Block


class Step(BaseModel):
    id: Optional[int] = None
    lesson: int
    position: int
    status: str
    block: Block

    class Config:
        extra = "ignore"
