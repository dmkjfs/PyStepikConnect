import requests
from typing import Optional, List

from pystepikconnect.types import Course, Lesson, Unit, Step, Section
from pystepikconnect.models import RequestParameters, Token
from pystepikconnect.core import courses, lessons, steps, sections, units, get_token
from pystepikconnect.exceptions import AuthorizationError


class SyncStepik:
    def __init__(self, client_id: str, client_secret: str) -> None:

        """
        Synchronous Stepik REST API client

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
        self.token = Token(**data)

    def request(self, params: RequestParameters) -> dict:

        """
        Synchronous requesting function. You can use it with any method from official documentation
        on https://stepik.org/api/docs if that method doesn't exist here

        :param params: all parameters for sending request
        """

        response = requests.api.request(
            method=params.method,
            url=f"{self.base_url}{'/' if params.path.startswith('') else ''}{params.path}",
            params=params.params,
            data=params.data,
            headers=params.headers,
            auth=params.auth
        )

        return response.json()

    def get_courses(self) -> List[Course]:

        """
        Gets your courses

        :return: list of courses
        """

        data = self.request(courses.get(token=self.token.access_token))
        return list(map(lambda course: Course(**course), data["courses"]))

    def create_course(self, course: Course) -> int:

        """
        Creates a new course

        :param course: course object
        :return: new course id
        """

        data = self.request(courses.create(token=self.token.access_token, course=course))
        return data["courses"][0]["id"]

    def update_course(self, course: Course) -> int:

        """
        Updates existing course

        :param course: updated course object. **Do not specify step id in it**
        :return: course id
        """

        data = self.request(courses.update(token=self.token.access_token, course=course))
        return data["courses"][0]["id"]

    def get_sections(self, course_id: int) -> List[Section]:

        """
        Gets sections from specified course

        :return: list of courses
        """

        if not isinstance(course_id, int):
            raise TypeError("Invalid value for argument")

        data = self.request(sections.get(token=self.token.access_token, course_id=course_id))
        return list(map(lambda section: Section(**section), data["sections"]))

    def create_section(self, section: Section) -> int:

        """
        Creates a section in course

        :param section: section object
        :return: new section id
        """

        data = self.request(sections.create(token=self.token.access_token, section=section))
        return data["sections"][0]["id"]

    def update_section(self, section: Section) -> int:

        """
        Updates existing section

        :param section: updated section object. **Do not specify step id in it**
        :return: section id
        """

        data = self.request(sections.update(token=self.token.access_token, section=section))
        return data["courses"][0]["id"]

    def get_units(self, course_id: int, lesson_id: int) -> List[Unit]:

        """
        Gets units in specified lesson

        :param lesson_id: id of a lesson you want to get units from
        :param course_id: id of a course where that lesson is placed
        :return: list of units
        """

        if not isinstance(course_id, int) or not isinstance(lesson_id, int):
            raise TypeError("Invalid value for argument")

        data = self.request(units.get(token=self.token.access_token, course_id=course_id, lesson_id=lesson_id))
        return list(map(lambda unit: Unit(**unit), data["units"]))

    def create_unit(self, unit: Unit) -> int:

        """
        Creates a new unit in lesson

        :param unit: unit object
        :return: new unit id
        """

        data = self.request(units.create(token=self.token.access_token, unit=unit))
        return data["courses"][0]["id"]

    def update_unit(self, unit: Unit) -> int:

        """
        Updates existing unit

        :param unit: updated unit object. **Do not specify step id in it**
        :return: unit id
        """

        data = self.request(units.update(token=self.token.access_token, unit=unit))
        return data["courses"][0]["id"]

    def get_lessons(self, course_id: Optional[int] = None) -> List[Lesson]:

        """
        Gets lessons in specified course

        :param course_id: course id
        :type course_id: int
        :return: list of lessons in course
        """

        if not isinstance(course_id, int | None):
            raise TypeError("Invalid value for argument: course_id")

        data = self.request(lessons.get(token=self.token.access_token, course_id=course_id))
        return list(map(lambda lesson: Lesson(**lesson), data["lessons"]))

    def create_lesson(self, lesson: Lesson) -> int:

        """
        Creates a new lesson

        :param lesson: object of Lesson with lesson parameters. **Do not specify lesson id in it**
        :return: lesson id
        """

        data = self.request(params=lessons.create(token=self.token.access_token, lesson=lesson))
        return data["lessons"][0]["id"]

    def update_lesson(self, lesson: Lesson) -> int:

        """
        Updates existing lesson

        :param lesson: updated lesson object. **Do not specify step id in it**
        :return: lesson id
        """

        data = self.request(lessons.update(token=self.token.access_token, lesson=lesson))
        return data["lessons"][0]["id"]

    def get_steps(self, lesson_id: Optional[int] = None) -> List[Step]:

        """
        Gets steps in a specified lesson

        :param lesson_id: id of a lesson you want to get steps from
        :return: list of steps in lesson
        """

        if not isinstance(lesson_id, int | None):
            raise TypeError("Invalid value for argument: course_id")

        data = self.request(steps.get(token=self.token.access_token, lesson_id=lesson_id))
        return list(map(lambda step: Step(**step), data["steps"]))

    def add_step(self, step: Step) -> int:

        """
        Adds new theory step to lesson

        :param step: new step object. **Do not specify step id in it**
        :return: step id
        """

        data = self.request(steps.create(token=self.token.access_token, step=step))
        return data["step-sources"][0]["id"]

    def update_step(self, step: Step) -> int:

        """
        Updates existing theory step from lesson

        :param step: updated step object. **Do not specify step id in it**
        :return: step id
        """

        data = self.request(steps.update(token=self.token.access_token, step=step))
        return data["step-sources"][0]["id"]
