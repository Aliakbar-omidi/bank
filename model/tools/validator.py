import  re

def name_validator(title, message):
    if isinstance(title, str) and re.match(r"^[a-zA-Z\s]{3,30}$"):
        return title
    else:
        raise ValueError(message)

def id_validator(id, message):
    if re.match(r"^\d{3,20}$", id):
        return id
    else:
        raise ValueError(message)