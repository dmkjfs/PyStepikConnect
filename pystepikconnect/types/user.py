from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    profile: int
    is_private: bool
    is_active: bool
    is_guest: bool
    is_organization: bool
    is_author: bool
    short_bio: str
    details: str
    first_name: str
    last_name: str
    full_name: str
    knowledge: int
    reputation: int
    created_courses_count: int
    created_lessons_count: int

    model_config = ConfigDict(extra='ignore')
