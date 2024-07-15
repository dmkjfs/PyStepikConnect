from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.enums import RequestMethod


def get(token: Token, user_id: int) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path=f"/api/users/{user_id}",
        headers={"Authorization": f"{token.token_type} {token.access_token}"}
    )
