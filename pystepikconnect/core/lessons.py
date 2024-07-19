from typing import Optional

from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Lesson


def get(token: Token, course_id: Optional[int] = None) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/lessons",
        params={"course": course_id},
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        }
    )


def create(token: Token, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/lessons",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"lesson": lesson.model_dump()}
    )


def update(token: Token, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/lessons/{lesson.id}",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"lesson": lesson.model_dump()}
    )
