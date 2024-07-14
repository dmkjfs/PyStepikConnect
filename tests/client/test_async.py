import pytest

from pystepikconnect.client.asynchronous import AsyncStepik
from pystepikconnect.exceptions import AuthorizationError


def test_auth(client_id: str) -> None:
    with pytest.raises(AuthorizationError):
        AsyncStepik(client_id=client_id, client_secret='')


@pytest.mark.asyncio
async def test_get_courses(async_stepik: AsyncStepik) -> None:
    assert isinstance(await async_stepik.get_courses(), list)


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
