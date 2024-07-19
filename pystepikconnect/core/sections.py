from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Section


def get(token: Token, course_id: int) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/sections",
        params={"course": course_id},
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        }
    )


def create(token: Token, section: Section) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"section": section.model_dump()}
    )


def update(token: Token, section: Section) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/sections/{section.id}",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"section": section.model_dump()}
    )
