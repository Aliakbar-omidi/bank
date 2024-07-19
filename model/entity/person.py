from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Date
from model.entity import *
from sqlalchemy.orm import relationship
from model.tools.validator import *


class Person(Base):
    __tablename__ = 'person_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _national_id = Column("national_id", Integer)
    _birthday = Column("birthday", Date)
    _phone = Column("phone", Integer)
    _email = Column("email", String(30))

    def __init__(self, name, family, national_id, birthday, phone, email):
        self.id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birthday = birthday
        self.phone = phone
        self.email = email

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name_validator(name, "Invalid name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = family

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id = national_id

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def set_phone(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email_validator(email, "Invalid email")