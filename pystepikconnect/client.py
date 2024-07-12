import requests
from typing import Optional, Dict, List, Any

from pystepikconnect.models import Lesson


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

        response = requests.post(
            url=f"{self.base_url}/oauth2/token/",
            data={"grant_type": "client_credentials"},
            auth=(client_id, client_secret)
        )

        data = response.json()
        self.token = data["access_token"]

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> dict:

        """
        Base `get` function. You can use it with any GET method from official documentation
        on https://stepik.org/api/docs if that method doesn't exist here
        """

        url = f"{self.base_url}{'/' if path.startswith('') else ''}{path}\
            ?{(''.join([param + '=' + value + '&' for param, value in params])) if params is not None else ''}"
        headers = requests.utils.default_headers()
        headers.update({"Authorization": f"Bearer {self.token}"})

        response = requests.get(url=url, headers=headers)
        return response.json()

    def post(self, path: str, data: dict) -> dict:

        """
        Base `post` function. You can use it with any POST method from official documentation
        on https://stepik.org/api/docs if that method doesn't exist here
        """

        url = f"{self.base_url}{'/' if path.startswith('') else ''}{path}"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.post(url=url, headers=headers, json=data)
        return response.json()

    def put(self, path: str, data: dict) -> dict:

        """
        Base `put` function. You can use it with any PUT method from official documentation
        on https://stepik.org/api/docs if that method doesn't exist here
        """

        url = f"{self.base_url}{'/' if path.startswith('') else ''}{path}"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.put(url=url, headers=headers, json=data)
        return response.json()

    def get_courses(self) -> list:

        """
        Gets your courses

        :return: list of courses
        """

        path = "/api/courses"
        data = self.get(path=path)
        return data["courses"]

    def create_course(self):
        pass

    def update_course(self):
        pass

    def get_units(self):
        pass

    def create_unit(self):
        pass

    def update_unit(self):
        pass

    def get_lessons(self, course_id: int) -> List[Lesson]:

        """
        Gets lessons in specified course

        :param course_id: course id
        :return: list of lessons in course
        """

        path = "/api/lessons"

        data = self.get(path=path)
        return data["lessons"]

    def create_lesson(self, title: str) -> int:

        """
        Creates a new lesson

        :param title: your new lesson's title
        :return: lesson id
        """

        path = "/api/lessons"
        data = {"lesson": {"title": title}}

        data = self.post(path=path, data=data)
        return data["lessons"][0]["id"]

    def get_steps(self):
        pass

    def add_step(self, lesson_id: int, name: str, text: str, poll: Optional[dict] = None) -> int:

        """
        Adds new theory step to this lesson

        :param lesson_id: id of a lesson you want to insert a step into
        :param name: new step name
        :param text: text step
        :param poll: (optional) poll for step
        :return: step id
        """

        path = "/api/step-sources"
        data = {
            "stepSource": {
                "block": {
                    "name": name,
                    "text": text,
                    "source": poll  
                },
                "lesson": lesson_id,
                "position": 1
            }

        }

        data = self.post(path=path, data=data)
        return data["step-sources"][0]["id"]

    def update_step(self, lesson_id: int, step_id: int, name: str, text: str):

        """
        Updates existing theory step from lesson

        :param lesson_id: id of a lesson which contains the step
        :param step_id: id of the step you want to change
        :param name: new step name
        :param text: new step text
        :return: step id
        """

        path = f"/api/step-sources/{step_id}"
        data = {
            "stepSource": {
                "block": {
                    "name": name,
                    "text": text
                },
                "lesson": lesson_id,
                "position": 1
            }
        }

        data = self.put(path=path, data=data)
        return data["step-sources"][0]["id"]
