from enum import Enum


class RequestMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
