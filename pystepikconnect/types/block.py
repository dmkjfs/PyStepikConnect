from pydantic import BaseModel
from pystepikconnect.types.source import Source


class Block(BaseModel):
    name: str
    text: str
    source: Source

    class Config:
        extra = "ignore"
