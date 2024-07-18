import pytest

from pystepikconnect.client.asynchronous import AsyncStepik
from pystepikconnect.client.synchronous import SyncStepik
from pystepikconnect.exceptions import AuthorizationError
from pystepikconnect.types import Step, User, Course, Section, Lesson, Unit, Block, Source, Option


@pytest.mark.parametrize("fake_client_secret", ["fake_secret_1", "fake_secret_2"])
def test_auth(client_id: str, fake_client_secret: str) -> None:
    with pytest.raises(AuthorizationError):
        AsyncStepik(client_id=client_id, client_secret=fake_client_secret)


@pytest.mark.asyncio
async def test_get_me(async_stepik: AsyncStepik) -> None:
    me = await async_stepik.get_me()
    assert isinstance(me, User)


@pytest.fixture
def me(stepik: SyncStepik) -> User:
    return stepik.get_me()


@pytest.mark.asyncio
async def test_get_user(async_stepik: AsyncStepik, me: User) -> None:
    assert isinstance(await async_stepik.get_user(user_id=me.id), User)


@pytest.mark.asyncio
async def test_create_course(async_stepik: AsyncStepik) -> None:
    course = Course(
        title='title',
        summary='summary',
        intro='intro',
        workload='workload',
        course_format='format',
        description='description'
    )
    course_id = await async_stepik.create_course(course=course)
    assert isinstance(course_id, int)


@pytest.fixture
def _course_id(stepik: SyncStepik) -> int:
    course = Course(
        title='title',
        summary='summary',
        intro='intro',
        workload='workload',
        course_format='format',
        description='description'
    )
    course_id = stepik.create_course(course=course)
    return course_id


@pytest.mark.asyncio
async def test_update_course(stepik: SyncStepik, _course_id: int) -> None:
    course = Course(
        id=_course_id,
        title='title_',
        summary='summary_',
        intro='intro_',
        workload='workload_',
        course_format='format_',
        description='description_'
    )
    course_id = stepik.update_course(course=course)
    assert isinstance(course_id, int)


@pytest.fixture
def course_id(stepik: SyncStepik, _course_id: int) -> int:
    course = Course(
        id=_course_id,
        title='title_',
        summary='summary_',
        intro='intro_',
        workload='workload_',
        course_format='format_',
        description='description_'
    )
    course_id = stepik.update_course(course=course)
    return course_id


@pytest.mark.asyncio
async def test_create_section(async_stepik: AsyncStepik) -> None:
    section = Section()
    section_id = await async_stepik.create_section(section=section)
    assert isinstance(section_id, int)


@pytest.fixture
def _section_id(stepik: SyncStepik) -> int:
    section = Section()
    section_id = stepik.create_section(section=section)
    return section_id


@pytest.mark.asyncio
async def test_update_section(async_stepik: AsyncStepik, _section_id: int) -> None:
    section = Section(id=_section_id)
    section_id = await async_stepik.update_section(section=section)
    assert isinstance(section_id, int)


@pytest.fixture
def section_id(stepik: SyncStepik, _section_id: int) -> int:
    section = Section(id=_section_id)
    section_id = stepik.update_section(section=section)
    return section_id


@pytest.mark.asyncio
async def test_create_lesson(async_stepik: AsyncStepik, course_id: int) -> None:
    lesson = Lesson(title="title", courses=[course_id])
    lesson_id = await async_stepik.create_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)


@pytest.fixture
def _lesson_id(stepik: SyncStepik, course_id: int) -> int:
    lesson = Lesson(title="title", courses=[course_id])
    lesson_id = stepik.create_lesson(lesson=lesson)
    return lesson_id


@pytest.mark.asyncio
async def test_update_lesson(async_stepik: AsyncStepik, course_id: int, _lesson_id: int) -> None:
    lesson = Lesson(id=_lesson_id, title="title_", courses=[course_id])
    lesson_id = await async_stepik.update_lesson(lesson=lesson)
    assert isinstance(lesson_id, int)


@pytest.fixture
def lesson_id(stepik: SyncStepik, course_id: int) -> int:
    lesson = Lesson(title="title_", courses=[course_id])
    lesson_id = stepik.update_lesson(lesson=lesson)
    return lesson_id


@pytest.mark.asyncio
async def test_create_unit(async_stepik: AsyncStepik, section_id: int, lesson_id: int) -> None:
    unit = Unit(section=section_id, lesson=lesson_id)
    unit_id = await async_stepik.create_unit(unit=unit)
    assert isinstance(unit_id, int)


@pytest.fixture
def _unit_id(stepik: SyncStepik, section_id: int, lesson_id: int) -> int:
    unit = Unit(section=section_id, lesson=lesson_id)
    unit_id = stepik.create_unit(unit=unit)
    return unit_id


@pytest.mark.asyncio
async def test_update_unit(async_stepik: AsyncStepik, _unit_id: int, section_id: int, lesson_id: int) -> None:
    unit = Unit(id=_unit_id, section=section_id, lesson=lesson_id)
    unit_id = await async_stepik.update_unit(unit=unit)
    assert isinstance(unit_id, int)


@pytest.fixture
def unit_id(stepik: SyncStepik, section_id: int, lesson_id: int, _unit_id: int) -> int:
    unit = Unit(id=_unit_id, section=section_id, lesson=lesson_id)
    unit_id = stepik.update_unit(unit=unit)
    return unit_id


@pytest.mark.asyncio
async def test_create_step(async_stepik: AsyncStepik, lesson_id: int) -> None:
    step = Step(
        lesson=lesson_id,
        position=1,
        status="status",
        block=Block(
            name="name",
            text="text"
        )
    )
    step_id = await async_stepik.create_step(step=step)
    assert isinstance(step_id, int)


@pytest.fixture
def _step_id(stepik: SyncStepik, lesson_id: int) -> int:
    step = Step(
        lesson=lesson_id,
        position=1,
        status="status",
        block=Block(
            name="name",
            text="text"
        )
    )
    step_id = stepik.create_step(step=step)
    return step_id


@pytest.mark.asyncio
async def test_update_step(async_stepik: AsyncStepik, _step_id: int, lesson_id: int) -> None:
    step = Step(
        id=_step_id,
        lesson=lesson_id,
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


@pytest.fixture
def step_id(stepik: SyncStepik, lesson_id: int, _step_id: int) -> int:
    step = Step(
        id=_step_id,
        lesson=lesson_id,
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
    step_id = stepik.create_step(step=step)
    return step_id


@pytest.mark.asyncio
async def test_get_courses(async_stepik: AsyncStepik, me: User) -> None:
    courses = await async_stepik.get_courses(owner_id=me.id)
    assert isinstance(courses, list)


@pytest.mark.asyncio
async def test_get_sections(async_stepik: AsyncStepik, course_id: int) -> None:
    assert isinstance(await async_stepik.get_sections(course_id=course_id), list)


@pytest.mark.asyncio
async def test_get_lessons(async_stepik: AsyncStepik, course_id: int) -> None:
    assert isinstance(await async_stepik.get_lessons(course_id=course_id), list)


@pytest.mark.asyncio
async def test_get_steps(async_stepik: AsyncStepik, lesson_id: int) -> None:
    assert isinstance(await async_stepik.get_steps(lesson_id=lesson_id), list)


@pytest.mark.asyncio
async def test_get_units(async_stepik: AsyncStepik, course_id: int, lesson_id: int) -> None:
    assert isinstance(await async_stepik.get_units(
        lesson_id=lesson_id,
        course_id=course_id
    ), list)
