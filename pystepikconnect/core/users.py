from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token


def get(token: Token, user_id: int) -> RequestParameters:
    # TODO: make user_id optional
    # TODO: add meta
    return RequestParameters(
        method=RequestMethod.GET,
        path=f"/api/users/{user_id}",
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        }
    )
