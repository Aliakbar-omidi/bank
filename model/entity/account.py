from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *


class Account(Base):
    __tablename__ = 'account'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _hesab_type = Column("hesab_type",String(30), nullable=False)
    _hesab_numbeer = Column("hesab_numbeer",String(30), nullable=False)

    def __init__(self, hesab_type, hesab_numbeer):
        self.id = None
        self._hesab_type = hesab_type
        self._hesab_numbeer = hesab_numbeer

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_hesab_type(self):
        return self._hesab_type

    def set_hesab_type(self, hesab_type):
        self._hesab_type = hesab_type

    def get_hesab_number(self):
        return self._hesab_numbeer

    def set_hesab_number(self, hesab_numbeer):
        self._hesab_numbeer = hesab_numbeer

    id = property(get_id, set_id)
    hesab_type = property(get_hesab_type, set_hesab_type)
    hesab_numbeer = property(get_hesab_number,set_hesab_number)