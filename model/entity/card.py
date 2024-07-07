from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *
import re


class Bank(Base):
    __tablename__ = "bank_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("title", String(20), nullable=False)
    _location = Column("location", String(20), nullable=False)
    _start_work = Column("start_date", DateTime)
    _end_work = Column("end_date", DateTime)

    def __init__(self, number_card, cvv2, expiretion_date, password ):
        self.id = None
        self.number_card = number_card
        self.cvv2 = cvv2
        self.expiretion_date = expiretion_date
        self.password = password


    def get_id(self):
        return self._id

    def set_id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("id must be an integer")

    def get_number_card(self):
        return self._number_card

    def set_number_card(self, number_card):
        self._number_card = number_card

    def get_cvv2(self):
        return self._cvv2

    def set_cvv2(self, cvv2):
        self._cvv2 = cvv2

    def get_expiretion_date(self):
        return self._expiretion_date

    def set_expiretion_date(self, expiretion_date):
        self._expiretion_date = expiretion_date

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    id = property(get_id, set_id)
    number_card = property(get_number_card, set_number_card)
    cvv2 = property(get_cvv2, set_cvv2)
    expiretion_date = property(get_expiretion_date, set_expiretion_date)
    password = property(get_password, set_password)