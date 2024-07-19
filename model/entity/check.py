from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Date
from model.entity import *
from sqlalchemy.orm import relationship
from model.tools.validator import *


class Check(Base):
    __tablename__ = 'check_tbl'
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _check_serial = Column("check_serial", Integer)
    _price = Column("price", Integer)
    _national_id = Column("national_id", Integer, unique=True)
    _date_now = Column("date_now", Date)
    _date_end = Column("date_end", Date)

    # _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    # account = relationship("Account")

    def __init__(self, check_serial, price, national_id, date_now, date_end):
        self.id = None
        self.check_serial = check_serial
        self.price = price
        self.national_id = national_id
        self.date_now = date_now
        self.date_end = date_end

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def check_serial(self):
        return self._check_serial

    @check_serial.setter
    def check_serial(self,check_serial):
        self._check_serial = check_serial

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        self._price = price

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id = int_validator(national_id, "Invalid id")

    @property
    def date_now(self):
        return self._date_now

    @date_now.setter
    def date_now(self, date_now):
        self._date_now = date_validator(date_now,"Invalid date")

    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        self._date_end = date_validator(date_end,"Invalid date")