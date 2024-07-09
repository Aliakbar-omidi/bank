from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *


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

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_hesab_type(self):
        return self._hesab_type

    def set_hesab_type(self, hesab_type):
        self._hesab_type = hesab_type

    def get_hesab_number(self):
        return self._hesab_number

    def set_hesab_number(self, hesab_number):
        self._hesab_number = hesab_number

    id = property(get_id, set_id)
    hesab_type = property(get_hesab_type, set_hesab_type)
    hesab_number = property(get_hesab_number,set_hesab_number)