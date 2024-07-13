from pydantic import BaseModel


class Unit(BaseModel):
    id: int
    section: int
    lesson: int

    class Config:
        extra = "ignore"
