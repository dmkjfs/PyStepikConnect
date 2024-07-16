from typing import Union


def dict_to_query(params: Union[dict, None]) -> str:
    return "?" + "&".join([f"{param}={value}" for param, value in params.items()]) if params is not None else ''
