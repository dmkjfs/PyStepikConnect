from typing import Optional

from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.types import Step


def get(token: Token, lesson_id: Optional[int] = None) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/steps",
        params={"lesson": lesson_id},
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        }
    )


def create(token: Token, step: Step) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/step-sources",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"stepSource": step.model_dump()}
    )


def update(token: Token, step: Step) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/step-sources/{step.id}",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        },
        data={"stepSource": step.model_dump()}
    )
