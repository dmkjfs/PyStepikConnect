import pytest

from unittest.mock import Mock

from pystepikconnect.client.synchronous import SyncStepik
from pystepikconnect.exceptions import AuthorizationError


def test_auth(client_id: str) -> None:
    with pytest.raises(AuthorizationError):
        SyncStepik(client_id=client_id, client_secret='')


def test_get_courses(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_courses(), list)


def test_get_sections(stepik: SyncStepik) -> None:
    course = stepik.get_courses()[0]
    assert isinstance(stepik.get_sections(course_id=course.id), list)


def test_get_lessons(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_lessons(), list)


def test_get_steps(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_steps(), list)


def test_get_units(stepik: SyncStepik) -> None:
    lessons = stepik.get_lessons()
    lesson = lessons[0]
    assert isinstance(stepik.get_units(lesson_id=lesson.id, course_id=lesson.courses[0]), list)


def test_create_course(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.create_course(course=mock), int)


def test_update_course(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.update_course(course=mock), int)


def test_create_section(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.create_section(section=mock), int)


def test_update_section(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.update_section(section=mock), int)


def test_create_lesson(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.create_lesson(lesson=mock), int)


def test_update_lesson(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.update_lesson(lesson=mock), int)


def test_create_unit(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.create_unit(unit=mock), int)


def test_update_unit(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.update_unit(unit=mock), int)


def test_create_step(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.create_step(step=mock), int)


def test_update_step(stepik: SyncStepik, mock: Mock) -> None:
    assert isinstance(stepik.update_step(step=mock), int)
