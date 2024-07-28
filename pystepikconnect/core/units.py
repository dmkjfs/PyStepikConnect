from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Unit


def get(token: Token, course_id: int, lesson_id: int, page: int = 1) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/units",
        params={
            "course": course_id,
            "lesson": lesson_id,
            "page": page
        },
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        }
    )


def create(token: Token, unit: Unit) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/units",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"unit": unit.model_dump()}
    )


def update(token: Token, unit: Unit) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/units/{unit.id}",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"unit": unit.model_dump()}
    )
