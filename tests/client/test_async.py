import pytest

from unittest.mock import AsyncMock

from pystepikconnect.client.asynchronous import AsyncStepik
from pystepikconnect.exceptions import AuthorizationError


def test_auth(client_id: str) -> None:
    with pytest.raises(AuthorizationError):
        AsyncStepik(client_id=client_id, client_secret='')


@pytest.mark.asyncio
async def test_get_courses(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_courses(), list)


@pytest.mark.asyncio
async def test_get_sections(async_stepik: AsyncStepik) -> None:
    courses = await async_stepik.get_courses()
    course = courses[0]
    assert isinstance(await async_stepik.get_sections(course_id=course.id), list)


@pytest.mark.asyncio
async def test_get_lessons(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_lessons(), list)


@pytest.mark.asyncio
async def test_get_steps(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_steps(), list)


@pytest.mark.asyncio
async def test_get_units(async_stepik: AsyncStepik) -> None:
    lessons = await async_stepik.get_lessons()
    lesson = lessons[0]
    assert isinstance(await async_stepik.get_units(lesson_id=lesson.id, course_id=lesson.courses[0]), list)


@pytest.mark.asyncio
async def test_create_course(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(async_stepik.create_course(course=await async_mock), int)


@pytest.mark.asyncio
async def test_update_course(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.update_course(course=await async_mock), int)


@pytest.mark.asyncio
async def test_create_section(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.create_section(section=await async_mock), int)


@pytest.mark.asyncio
async def test_update_section(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.update_section(section=await async_mock), int)


@pytest.mark.asyncio
async def test_create_lesson(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.create_lesson(lesson=await async_mock), int)


@pytest.mark.asyncio
async def test_update_lesson(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.update_lesson(lesson=await async_mock), int)


@pytest.mark.asyncio
async def test_create_unit(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.create_unit(unit=await async_mock), int)


@pytest.mark.asyncio
async def test_update_unit(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.update_unit(unit=await async_mock), int)


@pytest.mark.asyncio
async def test_create_step(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.create_step(step=await async_mock), int)


@pytest.mark.asyncio
async def test_update_step(async_stepik: AsyncStepik, async_mock: AsyncMock) -> None:
    assert isinstance(await async_stepik.update_step(step=await async_mock), int)
