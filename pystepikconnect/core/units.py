from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Unit
from pystepikconnect.utils import model_to_dict


def get(token: Token, course_id: int, lesson_id: int) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/units",
        params={"course": course_id, "lesson": lesson_id},
        headers={"Authorization": f"{token.token_type} {token.access_token}"}
    )


def create(token: Token, unit: Unit) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/units",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"unit": model_to_dict(unit)}
    )


def update(token: Token, unit: Unit) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/units/{unit.id}",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"unit": model_to_dict(unit)}
    )
