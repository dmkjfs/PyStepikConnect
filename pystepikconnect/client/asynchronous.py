import aiohttp
import requests

from typing import Union, Optional, List

from pystepikconnect.types import Course, Lesson, Unit, Step, Section
from pystepikconnect.models import RequestParameters
from pystepikconnect.core import courses, lessons, steps, sections, units, get_token
from pystepikconnect.exceptions import AuthorizationError


class AsyncStepik:

    def __init__(self, client_id: str, client_secret: str) -> None:

        """
        Asynchronous Stepik REST API client

        :param client_id: client id which you can get from one of your applications
        on https://stepik.org/oauth2/applications/
        :param client_secret: client secret which you can get from one of your applications
        on https://stepik.org/oauth2/applications/
        """

        self.base_url = "https://stepik.org"
        params = get_token(client_id, client_secret)

        response = requests.post(
            url=str(self.base_url+params.path),
            data=params.data,
            auth=(client_id, client_secret)
        )

        if response.status_code == 401:
            raise AuthorizationError('Incorrect credentials')

        data = response.json()
        self.token: str = data["access_token"]

    async def request(self, params: RequestParameters) -> dict:

        """
        Asynchronous requesting function. You can use it with any method from official documentation
        on https://stepik.org/api/docs if that method doesn't exist here

        :param params: all parameters for sending request
        """

        async with aiohttp.ClientSession(base_url=self.base_url) as session:
            async with session.request(
                method=params.method,
                url=params.path + "?" + "&".join([f"{param}={value}" for param, value in params.params.items()]),
                json=params.data,
                headers=params.headers
            ) as response:
                return await response.json()

    async def get_courses(self) -> List[Course]:

        """
        Gets your courses

        :return: list of courses
        """

        data = await self.request(courses.get(token=self.token))
        return list(map(lambda course: Course(**course), data["courses"]))

    async def create_course(self, course: Course) -> int:

        """
        Creates a new course

        :param course: course object
        :return: new course id
        """

        data = await self.request(courses.create(token=self.token, course=course))
        return data["courses"][0]["id"]

    async def update_course(self, course: Course) -> int:

        """
        Updates existing course

        :param course: updated course object. **Do not specify step id in it**
        :return: course id
        """

        data = await self.request(courses.update(token=self.token, course=course))
        return data["courses"][0]["id"]

    async def get_sections(self, course_id: int) -> List[Section]:

        """
        Gets sections from specified course

        :return: list of courses
        """

        if not isinstance(course_id, int):
            raise TypeError("Invalid value for argument")

        data = await self.request(sections.get(token=self.token, course_id=course_id))
        return list(map(lambda section: Section(**section), data["sections"]))

    async def create_section(self, section: Section) -> int:

        """
        Creates a section in course

        :param section: section object
        :return: new section id
        """

        data = await self.request(sections.create(token=self.token, section=section))
        return data["sections"][0]["id"]

    async def update_section(self, section: Section) -> int:

        """
        Updates existing section

        :param section: updated section object. **Do not specify step id in it**
        :return: section id
        """

        data = await self.request(sections.update(token=self.token, section=section))
        return data["courses"][0]["id"]

    async def get_units(self, course_id: int, lesson_id: int) -> List[Unit]:

        """
        Gets units in specified lesson

        :param lesson_id: id of a lesson you want to get units from
        :param course_id: id of a course where that lesson is placed
        :return: list of units
        """

        if not isinstance(course_id, int) or not isinstance(lesson_id, int):
            raise TypeError("Invalid value for argument")

        data = await self.request(units.get(token=self.token, course_id=course_id, lesson_id=lesson_id))
        return list(map(lambda unit: Unit(**unit), data["units"]))

    async def create_unit(self, unit: Unit) -> int:

        """
        Creates a new unit in lesson

        :param unit: unit object
        :return: new unit id
        """

        data = await self.request(units.create(token=self.token, unit=unit))
        return data["courses"][0]["id"]

    async def update_unit(self, unit: Unit) -> int:

        """
        Updates existing unit

        :param unit: updated unit object. **Do not specify step id in it**
        :return: unit id
        """

        data = await self.request(units.update(token=self.token, unit=unit))
        return data["courses"][0]["id"]

    async def get_lessons(self, course_id: Optional[int] = None) -> List[Lesson]:

        """
        Gets lessons in specified course

        :param course_id: course id
        :type course_id: int
        :return: list of lessons in course
        """

        if not isinstance(course_id, Union[int, None]):
            raise TypeError("Invalid value for argument: course_id")

        data = await self.request(lessons.get(self.token))
        return list(map(lambda lesson: Lesson(**lesson), data["lessons"]))

    async def create_lesson(self, lesson: Lesson) -> int:

        """
        Creates a new lesson

        :param lesson: object of Lesson with lesson parameters. **Do not specify lesson id in it**
        :return: lesson id
        """

        data = await self.request(params=lessons.create(token=self.token, lesson=lesson))
        return data["lessons"][0]["id"]

    async def update_lesson(self, lesson: Lesson) -> int:

        """
        Updates existing lesson

        :param lesson: updated lesson object. **Do not specify step id in it**
        :return: lesson id
        """

        data = await self.request(lessons.update(token=self.token, lesson=lesson))
        return data["lessons"][0]["id"]

    async def get_steps(self, lesson_id: Optional[int] = None) -> List[Step]:

        """
        Gets steps in a specified lesson

        :param lesson_id: id of a lesson you want to get steps from
        :return: list of steps in lesson
        """

        if not isinstance(lesson_id, Union[int, None]):
            raise TypeError("Invalid value for argument: course_id")

        data = await self.request(steps.get(token=self.token, lesson_id=lesson_id))
        return list(map(lambda step: Step(**step), data["steps"]))

    async def add_step(self, step: Step) -> int:

        """
        Adds new theory step to lesson

        :param step: new step object. **Do not specify step id in it**
        :return: step id
        """

        data = await self.request(steps.create(token=self.token, step=step))
        return data["step-sources"][0]["id"]

    async def update_step(self, step: Step) -> int:

        """
        Updates existing theory step from lesson

        :param step: updated step object. **Do not specify step id in it**
        :return: step id
        """

        data = await self.request(steps.update(token=self.token, step=step))
        return data["step-sources"][0]["id"]