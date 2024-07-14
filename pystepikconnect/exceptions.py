from logging import getLogger


logger = getLogger("pystepikconnect")


class AuthorizationError(Exception):
    """
    Incorrect credentials - `client_id` or `client_secre`
    """
