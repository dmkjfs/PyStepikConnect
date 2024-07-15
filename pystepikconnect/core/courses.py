from typing import Optional

from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.enums import RequestMethod
from pystepikconnect.types import Course


def get(token: Token, owner_id: Optional[int] = None) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/courses",
        params={"owner": owner_id},
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
    )


def create(token: Token, course: Course) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/courses",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"course": course.model_dump()}
    )


def update(token: Token, course: Course) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/courses/{course.id}",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"course": course.model_dump()}
    )
