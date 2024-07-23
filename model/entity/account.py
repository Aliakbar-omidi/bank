
from model.entity import *


class Account(Base):
    __tablename__ = 'account_tbl'
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _hesab_type = Column("hesab_type", String(30), nullable=False)
    _hesab_number = Column("hesab_number", Integer , default=0, nullable=False)

    _person_id = Column("person_id", Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")

    _bank_id = Column("bank_id",Integer, ForeignKey("bank_tbl.id"))
    bank = relationship("Bank")

    def __init__(self, hesab_type, hesab_number):
        self.id = None
        self.hesab_type = hesab_type
        self.hesab_number = hesab_number
        self.person_id = None
        self.bank_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def hesab_type(self):
        return self._hesab_type

    @hesab_type.setter
    def hesab_type(self, hesab_type):
        self._hesab_type = hesab_type

    @property
    def hesab_number(self):
        return self._hesab_number

    @hesab_number.setter
    def hesab_number(self, hesab_number):
        self._hesab_number = hesab_number

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id

    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        self._bank_id = bank_id
