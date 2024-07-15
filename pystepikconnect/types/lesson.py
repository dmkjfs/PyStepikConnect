from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from pystepikconnect.types.step import Step


class Lesson(BaseModel):
    id: Optional[int] = None
    title: str
    steps: Optional[List[Step]] = None
    courses: Optional[List[int]] = None
    units: Optional[List[int]] = None

    model_config = ConfigDict(extra='ignore')
