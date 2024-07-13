from pydantic import BaseModel
from typing import Optional

from pystepikconnect.enums import RequestMethod


class RequestParameters(BaseModel):
    method: RequestMethod
    path: str
    params: Optional[dict] = None
    auth: Optional[tuple] = None
    headers: Optional[dict] = None
    data: Optional[dict] = None
