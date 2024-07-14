from pystepikconnect.models import RequestParameters
from pystepikconnect.enums import RequestMethod
from pystepikconnect.types import Unit


def get(token: str, course_id: int, lesson_id: int) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/units",
        params={"course": course_id, "lesson": lesson_id},
        headers={"Authorization": f"Bearer {token}"},
    )


def create(token: str, unit: Unit) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/units",
        headers={"Authorization": f"Bearer {token}"},
        data={"unit": unit.model_dump()}
    )


def update(token: str, unit: Unit) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/units/{unit.id}",
        headers={"Authorization": f"Bearer {token}"},
        data={"unit": unit.model_dump()}
    )