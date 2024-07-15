import pytest

from pystepikconnect.client.synchronous import SyncStepik
from pystepikconnect.exceptions import AuthorizationError
from pystepikconnect.types import Step, User, Course, Section, Lesson, Unit, Block, Source, Option


@pytest.mark.parametrize("fake_client_secret", ["fake_secret_1", "fake_secret_2"])
def test_auth(client_id: str, fake_client_secret: str) -> None:
    with pytest.raises(AuthorizationError):
        SyncStepik(client_id=client_id, client_secret=fake_client_secret)


def test_get_me(stepik: SyncStepik) -> int:
    me = stepik.get_me()
    assert isinstance(me, User)
    return me.id


def test_get_user(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_user(user_id=test_get_me(stepik=stepik)), User)


def test_create_course(stepik: SyncStepik) -> int:
    course = Course(
        summary='summary',
        intro='intro',
        workload='workload',
        course_format='format',
        description='description'
    )
    course_id = stepik.create_course(course=course)
    assert isinstance(course_id, int)
    return course_id


def test_update_course(stepik: SyncStepik) -> int:
    course = Course(
        id=test_create_course(stepik=stepik),
        summary='summary_',
        intro='intro_',
        workload='workload_',
        course_format='format_',
        description='description_'
    )
    course_id = stepik.update_course(course=course)
    assert isinstance(course_id, int)
    return course_id


def test_create_section(stepik: SyncStepik) -> int:
    section = Section()
    section_id = stepik.create_section(section=section)
    assert isinstance(section_id, int)
    return section_id


def test_update_section(stepik: SyncStepik) -> int:
    section = Section(id=test_create_section(stepik=stepik))
    section_id = stepik.update_section(section=section)
    assert isinstance(section_id, int)
    return section_id


def test_create_lesson(stepik: SyncStepik) -> int:
    lesson = Lesson(title="title", courses=[test_update_course(stepik=stepik)])
    lesson_id = stepik.create_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)
    return lesson_id


def test_update_lesson(stepik: SyncStepik) -> int:
    lesson = Lesson(id=test_create_lesson(stepik=stepik), title="title_", courses=[test_update_course(stepik=stepik)])
    lesson_id = stepik.update_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)
    return lesson_id


def test_create_unit(stepik: SyncStepik) -> int:
    unit = Unit(
        section=test_update_section(stepik=stepik),
        lesson=test_update_lesson(stepik=stepik),
    )
    unit_id = stepik.create_unit(unit=unit)
    assert isinstance(unit_id, int)
    return unit_id


def test_update_unit(stepik: SyncStepik) -> int:
    unit = Unit(
        id=test_create_unit(stepik=stepik),
        section=test_update_section(stepik=stepik),
        lesson=test_update_lesson(stepik=stepik),
    )
    unit_id = stepik.update_unit(unit=unit)
    assert isinstance(unit_id, int)
    return unit_id


def test_create_step(stepik: SyncStepik) -> int:
    step = Step(
        lesson=test_update_lesson(stepik=stepik),
        position=1,
        status="status",
        block=Block(
            name="name",
            text="text"
        )
    )
    step_id = stepik.create_step(step=step)
    assert isinstance(step_id, int)
    return step_id


def test_update_step(stepik: SyncStepik) -> int:
    step = Step(
        id=test_create_step(stepik=stepik),
        lesson=test_update_lesson(stepik=stepik),
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
    return step_id


def test_get_courses(stepik: SyncStepik) -> None:
    courses = stepik.get_courses(owner_id=test_get_me(stepik=stepik))
    assert isinstance(courses, list)


def test_get_sections(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_sections(course_id=test_update_course(stepik=stepik)), list)


def test_get_lessons(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_lessons(course_id=test_update_course(stepik=stepik)), list)


def test_get_steps(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_steps(lesson_id=test_update_lesson(stepik=stepik)), list)


def test_get_units(stepik: SyncStepik) -> None:
    assert isinstance(stepik.get_units(
        lesson_id=test_update_lesson(stepik=stepik),
        course_id=test_update_course(stepik=stepik)
    ), list)
