from typing import Union

from pydantic import BaseModel


def dict_to_query(params: Union[dict, None]) -> str:

    """
    Transforms dictionary with query params into query string

    :param params:
    """

    return "?" + "&".join([f"{param}={value}" for param, value in params.items()]) if params is not None else ''


def model_to_dict(model: BaseModel) -> dict:
    """
    Transforms Pydantic model into dictionaty and removes None items

    :param model: pydantic model you need to transform
    """

    return {key: item for key, item in model.model_dump().items() if item is not None}
