from logging import getLogger


logger = getLogger("pystepikconnect")


class AuthorizationError(Exception):
    """
    Invalid credentials
    """
