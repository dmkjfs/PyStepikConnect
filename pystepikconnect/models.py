from pydantic import BaseModel, ConfigDict
from typing import Optional

from pystepikconnect.enums import RequestMethod


class RequestParameters(BaseModel):
    method: RequestMethod
    path: str
    params: Optional[dict] = None
    auth: Optional[tuple] = None
    headers: Optional[dict] = None
    data: Optional[dict] = None


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

    model_config = ConfigDict(extra='ignore')
