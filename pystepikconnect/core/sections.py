from pystepikconnect.models import RequestParameters
from pystepikconnect.enums import RequestMethod
from pystepikconnect.types import Section


def get(token: str, course_id: int) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/sections",
        headers={"Authorization": f"Bearer {token}"},
    )


def create(token: str, section: Section) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/sections",
        headers={"Authorization": f"Bearer {token}"},
        data={"section": section.model_dump()}
    )


def update(token: str, section: Section) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/sections/{section.id}",
        headers={"Authorization": f"Bearer {token}"},
        data={"section": section.model_dump()}
    )
