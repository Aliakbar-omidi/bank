from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Date
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *

class Person(Base):
    __tablename__ = 'person_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name",String(30))
    family = Column("family", String(30))
    national_id = Column("national_id", Integer)
    birthday = Column("",Date)
    phone = Column("phone", Integer)
    email = Column("email", String(30))

    def __init__(self, name, family, national_id, birthday, phone, email):
        self.id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birthday = birthday
        self.phone = phone
        self.email = email

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def det_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_family(self):
        return self._family

    def set_family(self, family):
        self._family = family

    def get_national_id(self):
        return self._national_id

    def set_national_id(self, national_id):
        self._national_id = national_id

    def get_birthday(self):
        return self._birthday

    def set_birthday(self, birthday):
        self._birthday = birthday

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    id = property(get_id, set_id)
    name = property(det_name, set_name)
    family = property(get_family,set_family)
    national_id = property(get_national_id, set_national_id)
    birthday = property(get_birthday, set_birthday)
    phone = property(get_phone, set_phone)
    email = property(get_email, set_email)