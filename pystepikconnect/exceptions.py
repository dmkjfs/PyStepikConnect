class AuthorizationError(Exception):
    """
    Incorrect credentials - `client_id` or `client_secre`
    """


class NotFoundError(Exception):
    """
    Status code 404
    Not found
    """


class ForbiddenError(Exception):
    """
    Status code 403
    Not enough permissions
    """


class AuthorPermissionError(ForbiddenError):
    """
    Not enough permissions
    """
