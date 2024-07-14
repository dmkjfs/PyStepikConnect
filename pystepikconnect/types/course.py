from pydantic import BaseModel
from typing import Optional


class Course(BaseModel):
    id: Optional[int] = None
    summary: str
    intro: str
    course_format: str
    description: str
    total_units: int
    first_lesson: int
    first_unit: int
    lessons_count: int

    class Config:
        extra = "ignore"
