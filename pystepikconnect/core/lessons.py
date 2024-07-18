from typing import Optional

from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Lesson
from pystepikconnect.utils import model_to_dict


def get(token: Token, course_id: Optional[int] = None) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/lessons",
        params={"course": course_id},
        headers={"Authorization": f"{token.token_type} {token.access_token}"}
    )


def create(token: Token, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/lessons",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"lesson": model_to_dict(lesson)}
    )


def update(token: Token, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/lessons/{lesson.id}",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"lesson": model_to_dict(lesson)}
    )
