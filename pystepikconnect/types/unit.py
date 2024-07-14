from pydantic import BaseModel, ConfigDict


class Unit(BaseModel):
    id: int
    section: int
    lesson: int

    model_config = ConfigDict(extra='ignore')
