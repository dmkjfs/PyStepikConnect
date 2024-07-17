from typing import Optional

from pydantic import BaseModel, ConfigDict
from requests.auth import HTTPBasicAuth

from pystepikconnect.enums import RequestMethod


class RequestParameters(BaseModel):
    method: RequestMethod
    path: str
    params: Optional[dict] = None
    auth: Optional[HTTPBasicAuth] = None
    headers: Optional[dict] = None
    data: Optional[dict] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

    model_config = ConfigDict(extra='ignore')
