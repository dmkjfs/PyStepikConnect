from pydantic import BaseModel, ConfigDict
from typing import Optional


class Section(BaseModel):
    id: Optional[int] = None

    model_config = ConfigDict(extra='ignore')
