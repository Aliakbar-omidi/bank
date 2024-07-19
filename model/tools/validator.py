import re
from datetime import datetime,time, date


def name_validator(name, message):
    if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)


def boolean_validator(bool_value, message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)


def time_validator(time_value, message):
    if isinstance(time_value, time):
        return time_value
    else:
        raise ValueError(message)


def date_validator(date_value, message):
    if isinstance(date_value, date):
        return date_value
    else:
        raise ValueError(message)


def national_id__validator(natonal_id_value, message):
    if isinstance(natonal_id_value, str) and re.match(r"^\d{10}$", natonal_id_value):
        return natonal_id_value
    else:
        raise ValueError(message)


def email_validator(email_value, message):
    if isinstance(email_value, str) and re.match(r"^[a-zA-Z\s]+@(gmail|yahoo)\.com$", email_value):
        return email_value
    else:
        raise ValueError(message)