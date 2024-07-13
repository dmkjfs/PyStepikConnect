from pystepikconnect.types import Lesson
from pystepikconnect.enums import RequestMethod
from pystepikconnect.models import RequestParameters


def get(token: str) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/lessons",
        params=None,
        headers={"Authorization": f"Bearer {token}"},
        data=None
    )


def create(token: str, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/lessons",
        params=None,
        headers={"Authorization": f"Bearer {token}"},
        data={"lesson": lesson.model_dump()}
    )


def update(token: str, lesson: Lesson) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/lessons/{lesson.id}",
        headers={"Authorization": f"Bearer {token}"},
        data={"lesson": lesson.model_dump()}
    )
