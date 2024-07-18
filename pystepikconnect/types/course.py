from pydantic import BaseModel, ConfigDict
from typing import Optional


class Course(BaseModel):
    id: Optional[int] = None
    title: str
    summary: str
    intro: str
    workload: str
    course_format: str
    description: str
    total_units: Optional[int] = None
    first_lesson: Optional[int] = None
    first_unit: Optional[int] = None
    lessons_count: Optional[int] = None

    model_config = ConfigDict(extra='ignore')
