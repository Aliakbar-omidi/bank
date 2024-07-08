import  re

def name_validator(title, message):
    if isinstance(title, str) and re.match(r"^[a-zA-Z\s]{3,30}$"):
        return title
    else:
        raise ValueError(message)

def id_validator(id, message):
    if isinstance(id, int):
        return id
    else:
        raise ValueError(message)