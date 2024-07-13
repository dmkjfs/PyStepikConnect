from pystepikconnect.models import RequestParameters
from pystepikconnect.enums import RequestMethod
from pystepikconnect.types import Course


def get(token: str) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/courses",
        params={"is_featured": True},
        headers={"Authorization": f"Bearer {token}"},
    )


def create(token: str, course: Course) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/courses",
        headers={"Authorization": f"Bearer {token}"},
        data={"course": course.model_dump()}
    )


def update(token: str, course: Course) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/courses/{course.id}",
        headers={"Authorization": f"Bearer {token}"},
        data={"course": course.model_dump()}
    )
