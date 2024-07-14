from pydantic import BaseModel, ConfigDict
from typing import Optional
from pystepikconnect.types.source import Source


class Block(BaseModel):
    name: str
    text: str
    source: Optional[Source] = None

    model_config = ConfigDict(extra='ignore')
