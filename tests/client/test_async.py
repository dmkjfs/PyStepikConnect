import pytest

from unittest.mock import Mock

from pystepikconnect.client.asynchronous import AsyncStepik
from pystepikconnect.exceptions import AuthorizationError
from pystepikconnect.types import Step, User, Course, Section, Lesson, Unit, Block, Source, Option


params = {}


@pytest.mark.asyncio
async def test_auth(client_id: str) -> None:
    with pytest.raises(AuthorizationError):
        AsyncStepik(client_id=client_id, client_secret='')


@pytest.mark.asyncio
async def test_get_me(async_stepik: AsyncStepik) -> None:
    me = await async_stepik.get_me()
    assert isinstance(me, User)
    params['user'] = me.id


@pytest.mark.asyncio
async def test_get_user(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_user(user_id=params["user"]), User)


@pytest.mark.asyncio
async def test_create_course(async_stepik: AsyncStepik) -> None:
    course = Course(
        summary='summary',
        intro='intro',
        workload='workload',
        course_format='format',
        description='description'
    )
    course_id = await async_stepik.create_course(course=course)
    assert isinstance(course_id, int)
    params["course"] = course_id


@pytest.mark.asyncio
async def test_update_course(async_stepik: AsyncStepik) -> None:
    course = Course(
        summary='summary_',
        intro='intro_',
        workload='workload_',
        course_format='format_',
        description='description_'
    )
    course_id = await async_stepik.update_course(course=course)
    assert isinstance(course_id, int)
    params["course"] = course_id


@pytest.mark.asyncio
async def test_create_section(async_stepik: AsyncStepik) -> None:
    section = Section()
    section_id = await async_stepik.create_section(section=section)
    assert isinstance(section_id, int)
    params["section"] = section_id


@pytest.mark.asyncio
async def test_update_section(async_stepik: AsyncStepik, mock: Mock) -> None:
    section = Section()
    section_id = await async_stepik.update_section(section=section)
    assert isinstance(section_id, int)
    params["section"] = section_id


@pytest.mark.asyncio
async def test_create_lesson(async_stepik: AsyncStepik, mock: Mock) -> None:
    lesson = Lesson(title="title")
    lesson_id = await async_stepik.create_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)
    params["lesson"] = lesson_id


@pytest.mark.asyncio
async def test_update_lesson(async_stepik: AsyncStepik, mock: Mock) -> None:
    lesson = Lesson(title="title_")
    lesson_id = await async_stepik.update_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)
    params["lesson"] = lesson_id


@pytest.mark.asyncio
async def test_create_unit(async_stepik: AsyncStepik, mock: Mock) -> None:
    unit = Unit(
        section=params["section"],
        lesson=params["lesson"],
    )
    unit_id = await async_stepik.create_unit(unit=unit)
    assert isinstance(unit_id, int)
    params["unit"] = unit_id


@pytest.mark.asyncio
async def test_update_unit(async_stepik: AsyncStepik, mock: Mock) -> None:
    unit = Unit(
        section=params["section"],
        lesson=params["lesson"],
    )
    unit_id = await async_stepik.update_unit(unit=unit)
    assert isinstance(unit_id, int)
    params["unit"] = unit_id


@pytest.mark.asyncio
async def test_create_step(async_stepik: AsyncStepik, mock: Mock) -> None:
    step = Step(
        lesson=params["lesson"],
        position=1,
        status="status",
        block=Block(
            name="name",
            text="text"
        )
    )
    step_id = await async_stepik.create_step(step=step)
    assert isinstance(step_id, int)
    params["step"] = step_id


@pytest.mark.asyncio
async def test_update_step(async_stepik: AsyncStepik, mock: Mock) -> None:
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
    step_id = await async_stepik.update_step(step=step)
    assert isinstance(step_id, int)
    params["step"] = step_id


@pytest.mark.asyncio
async def test_get_courses(async_stepik: AsyncStepik) -> None:
    courses = await async_stepik.get_courses(owner_id=params["user"])
    assert isinstance(courses, list)


@pytest.mark.asyncio
async def test_get_sections(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_sections(course_id=params["course"]), list)


@pytest.mark.asyncio
async def test_get_lessons(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_lessons(course_id=params["course"]), list)


@pytest.mark.asyncio
async def test_get_steps(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_steps(lesson_id=params["lesson"]), list)


@pytest.mark.asyncio
async def test_get_units(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_units(lesson_id=params["lesson"], course_id=params["course"]), list)
