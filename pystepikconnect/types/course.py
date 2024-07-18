from pydantic import BaseModel, ConfigDict
from typing import Optional


class Course(BaseModel):
    id: Optional[int] = None
    title: str
    summary: Optional[str]
    intro: Optional[str]
    workload: Optional[str]
    course_format: Optional[str]
    description: Optional[str]
    total_units: Optional[int] = None
    first_lesson: Optional[int] = None
    first_unit: Optional[int] = None
    lessons_count: Optional[int] = None

    model_config = ConfigDict(extra='ignore')
