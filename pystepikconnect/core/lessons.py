from typing import Optional

from pystepikconnect.types import Lesson
from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters


def get(token: str, course_id: Optional[int] = None) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/lessons",
        params={'course': course_id},
        headers={"Authorization": f"Bearer {token}"},
    )


def create(token: str, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/lessons",
        headers={"Authorization": f"Bearer {token}"},
        data={"lesson": lesson.model_dump()}
    )


def update(token: str, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/lessons/{lesson.id}",
        headers={"Authorization": f"Bearer {token}"},
        data={"lesson": lesson.model_dump()}
    )
