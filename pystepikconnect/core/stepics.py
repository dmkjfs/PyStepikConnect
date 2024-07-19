from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters, Token


def get(token: Token) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path='/api/stepics/1',
        headers={
            "Authorization": f"{token.token_type} {token.access_token}",
            "Content-Type": "application/json"
        }
    )
