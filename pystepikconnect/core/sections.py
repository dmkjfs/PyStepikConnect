from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Section
from pystepikconnect.utils import model_to_dict


def get(token: Token, course_id: int) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/sections",
        params={"course": course_id},
        headers={"Authorization": f"{token.token_type} {token.access_token}"}
    )


def create(token: Token, section: Section) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/sections",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"section": model_to_dict(section)}
    )


def update(token: Token, section: Section) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/sections/{section.id}",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        data={"section": model_to_dict(section)}
    )
