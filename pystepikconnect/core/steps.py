from typing import Optional

from pystepikconnect.types import Step
from pystepikconnect.models import RequestParameters
from pystepikconnect.enums import RequestMethod


def get(token: str, lesson_id: Optional[int] = None) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.GET,
        path="/api/steps",
        params={"lesson": lesson_id},
        headers={"Authorization": f"Bearer {token}"},
    )


def create(token: str, step: Step) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.POST,
        path="/api/step-sources",
        headers={"Authorization": f"Bearer {token}"},
        data={"stepSource": {step.model_dump()}}
    )


def update(token: str, step: Step) -> RequestParameters:
    return RequestParameters(
        method=RequestMethod.PUT,
        path=f"/api/step-sources/{step.id}",
        headers={"Authorization": f"Bearer {token}"},
        data={"stepSource": {step.model_dump()}}
    )
