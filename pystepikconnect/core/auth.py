from requests.auth import HTTPBasicAuth

from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters


def get_token(client_id: str, client_secret: str) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/oauth2/token/",
        data={"grant_type": "client_credentials"},
        auth=HTTPBasicAuth(client_id, client_secret)
    )
