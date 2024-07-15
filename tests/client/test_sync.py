import pytest

from unittest.mock import Mock

from pystepikconnect.client.synchronous import SyncStepik
from pystepikconnect.exceptions import AuthorizationError
from pystepikconnect.types import Step, User, Course, Section, Lesson, Unit, Block, Source, Option


params = {}


def test_auth(client_id: str) -> None:
    with pytest.raises(AuthorizationError):
        SyncStepik(client_id=client_id, client_secret='')


def test_get_me(stepik: SyncStepik) -> None:
    me = stepik.get_me()
    assert isinstance(me, User)
    params['user'] = me.id


def test_get_user(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_user(user_id=params["user"]), User)


def test_create_course(stepik: SyncStepik) -> None:
    course = Course(
        summary='summary',
        intro='intro',
        workload='workload',
        course_format='format',
        description='description'
    )
    course_id = stepik.create_course(course=course)
    assert isinstance(course_id, int)
    params["course"] = course_id


def test_update_course(stepik: SyncStepik) -> None:
    course = Course(
        summary='summary_',
        intro='intro_',
        workload='workload_',
        course_format='format_',
        description='description_'
    )
    course_id = stepik.update_course(course=course)
    assert isinstance(course_id, int)
    params["course"] = course_id


def test_create_section(stepik: SyncStepik) -> None:
    section = Section()
    section_id = stepik.create_section(section=section)
    assert isinstance(section_id, int)
    params["section"] = section_id


def test_update_section(stepik: SyncStepik, mock: Mock) -> None:
    section = Section()
    section_id = stepik.update_section(section=section)
    assert isinstance(section_id, int)
    params["section"] = section_id


def test_create_lesson(stepik: SyncStepik, mock: Mock) -> None:
    lesson = Lesson(title="title")
    lesson_id = stepik.create_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)
    params["lesson"] = lesson_id


def test_update_lesson(stepik: SyncStepik, mock: Mock) -> None:
    lesson = Lesson(title="title_")
    lesson_id = stepik.update_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)
    params["lesson"] = lesson_id


def test_create_unit(stepik: SyncStepik, mock: Mock) -> None:
    unit = Unit(
        section=params["section"],
        lesson=params["lesson"],
    )
    unit_id = stepik.create_unit(unit=unit)
    assert isinstance(unit_id, int)
    params["unit"] = unit_id


def test_update_unit(stepik: SyncStepik, mock: Mock) -> None:
    unit = Unit(
        section=params["section"],
        lesson=params["lesson"],
    )
    unit_id = stepik.update_unit(unit=unit)
    assert isinstance(unit_id, int)
    params["unit"] = unit_id


def test_create_step(stepik: SyncStepik, mock: Mock) -> None:
    step = Step(
        lesson=params["lesson"],
        position=1,
        status="status",
        block=Block(
            name="name",
            text="text"
        )
    )
    step_id = stepik.create_step(step=step)
    assert isinstance(step_id, int)
    params["step"] = step_id


def test_update_step(stepik: SyncStepik, mock: Mock) -> None:
    step = Step(
        lesson=params["lesson"],
        position=1,
        status="status",
        block=Block(
            name="name_",
            text="text_",
            source=Source(
                options=[
                    Option(is_correct=True, text='option1', feedback='feedback1'),
                    Option(is_correct=False, text='option2', feedback='feedback2'),
                    Option(is_correct=False, text='option3', feedback='feedback3')
                ],
                is_always_correct=True,
                is_html_enabled=False,
                sample_size=3,
                is_multiple_choice=False,
                preserve_order=True,
                is_options_feedback=True
            )
        )
    )
    step_id = stepik.update_step(step=step)
    assert isinstance(step_id, int)
    params["step"] = step_id


def test_get_courses(stepik: SyncStepik) -> None:
    courses = stepik.get_courses(owner_id=params["user"])
    assert isinstance(courses, list)


def test_get_sections(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_sections(course_id=params["course"]), list)


def test_get_lessons(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_lessons(course_id=params["course"]), list)


def test_get_steps(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_steps(lesson_id=params["lesson"]), list)


def test_get_units(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_units(lesson_id=params["lesson"], course_id=params["course"]), list)
