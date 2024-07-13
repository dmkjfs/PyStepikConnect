from pystepikconnect.models import RequestParameters
from pystepikconnect.enums import RequestMethod


def get_token(client_id: str, client_secret: str):
    return RequestParameters(
        method=RequestMethod.POST,
        path="/oauth2/token/",
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    )
