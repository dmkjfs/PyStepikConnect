from typing import Optional

from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Course
from pystepikconnect.utils import model_to_dict


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
        data={"course": model_to_dict(course)}
    )


def update(token: Token, course: Course) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/courses/{course.id}",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"course": model_to_dict(course)}
    )
