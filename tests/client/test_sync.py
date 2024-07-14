import pytest

from pystepikconnect.client.synchronous import SyncStepik
from pystepikconnect.exceptions import AuthorizationError


def test_auth(client_id: str) -> None:
    with pytest.raises(AuthorizationError):
        SyncStepik(client_id=client_id, client_secret='')


def test_get_courses(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_courses(), list)


def test_get_lessons(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_lessons(), list)


def test_get_steps(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_steps(), list)


def test_get_units(stepik: SyncStepik) -> None:
    lessons = stepik.get_lessons()
    lesson = lessons[0]
    assert isinstance(stepik.get_units(lesson_id=lesson.id, course_id=lesson.courses[0]), list)
