from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.enums import RequestMethod


def get(token: Token) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path='/api/stepics/1',
        headers={"Authorization": f"{token.token_type} {token.access_token}"}
    )
