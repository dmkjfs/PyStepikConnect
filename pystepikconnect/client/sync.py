import requests
from typing import List

from pystepikconnect.types import Course, Lesson, Unit, Step
from pystepikconnect.models import RequestParameters
from pystepikconnect.core import courses, lessons, steps, units, get_token
from pystepikconnect.exceptions import AuthorizationError


class Stepik:
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
        self.token = data["access_token"]

    def request(self, params: RequestParameters) -> dict:

        """
        Base requesting function. You can use it with any method from official documentation
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

        data = self.request(courses.get(token=self.token))
        return list(map(lambda course: Course(**course), data["courses"]))

    def create_course(self):
        pass

    def update_course(self):
        pass

    def get_units(self, course_id: int, lesson_id: int) -> List[Unit]:

        """
        Gets units in specified course

        :param lesson_id: id of a lesson you want to get units from
        :param course_id: id of a course where that lesson is placed
        :return: list of units
        """

        if not isinstance(course_id, int):
            raise TypeError('Invalid value for argument: course_id')

        data = self.request(units.get(token=self.token, course_id=course_id))
        return list(map(lambda unit: Unit(**unit), data["units"]))

    def create_unit(self):
        pass

    def update_unit(self):
        pass

    def get_lessons(self, course_id: int) -> List[Lesson]:

        """
        Gets lessons in specified course

        :param course_id: course id
        :type course_id: int
        :return: list of lessons in course
        """

        if not isinstance(course_id, int):
            raise TypeError('Invalid value for argument: course_id')

        data = self.request(lessons.get(self.token))
        return list(map(lambda lesson: Lesson(**lesson), data["lessons"]))

    def create_lesson(self, lesson: Lesson) -> int:

        """
        Creates a new lesson

        :param lesson: object of Lesson with lesson parameters. **Do not specify lesson id in it**
        :return: lesson id
        """

        data = self.request(params=lessons.create(token=self.token, lesson=lesson))
        return data["lessons"][0]["id"]

    def update_lesson(self):
        pass

    def get_steps(self, lesson_id: int) -> List[Step]:

        """
        Gets steps in a specified lesson

        :param lesson_id: id of a lesson you want to get steps from
        :return: list of steps in lesson
        """

        if not isinstance(lesson_id, int):
            raise TypeError('Invalid value for argument: course_id')

        data = self.request(steps.get(token=self.token, lesson_id=lesson_id))
        return list(map(lambda step: Step(**step), data["steps"]))

    def add_step(self, step: Step) -> int:

        """
        Adds new theory step to lesson

        :param step: new step object. **Do not specify step id in it**
        :return: step id
        """

        data = self.request(steps.create(token=self.token, step=step))
        return data["step-sources"][0]["id"]

    def update_step(self, step: Step):

        """
        Updates existing theory step from lesson

        :param step: updated step object. **Do not specify step id in it**
        :return: step id
        """

        data = self.request(steps.update(token=self.token, step=step))
        return data["step-sources"][0]["id"]
