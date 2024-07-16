def dict_to_query(params: dict) -> str:
    return "?" + "&".join([f"{param}={value}" for param, value in params.items()]) if params is not None else ''
