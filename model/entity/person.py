
from model.entity import *


class Person(Base):
    __tablename__ = 'person_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _national_id = Column("national_id", Integer, unique=True)
    _birthdate = Column("birthdate", Date)
    _phone = Column("phone", Integer)
    _email = Column("email", String(30))

    account = relationship("Account",back_populates="person")

    def __init__(self, name, family, national_id, birthdate, phone, email):
        self.id = None
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birthdate = birthdate
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
        self._name = name

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
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self._birthdate = birthdate

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email_validator(email,"Invalid email")