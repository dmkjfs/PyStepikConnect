from pydantic import BaseModel
from typing import List


class Lesson(BaseModel):
    id: int
    title: str
    steps: list
    courses: List[int]
    units: List[int]

    class Config:
        extra = 'ignore'


class Course(BaseModel):
    id: int
    summary: str
    intro: str
    course_format: str
    description: str
    total_units: int
    first_lesson: int
    first_unit: int
    lessons_count: int

    class Config:
        extra = 'ignore'


class Unit(BaseModel):
    class Config:
        extra = 'ignore'
