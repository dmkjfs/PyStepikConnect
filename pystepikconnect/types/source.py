from pydantic import BaseModel
from typing import List


class Option(BaseModel):
    is_correct: bool
    text: str
    feedback: str

    class Config:
        extra = "ignore"


class Source(BaseModel):
    options: List[Option]
    is_always_correct: bool
    is_html_enabled: bool
    sample_size: int
    is_multiple_choice: bool
    preserve_order: bool
    is_options_feedback: bool

    class Config:
        extra = "ignore"
