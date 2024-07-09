from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Date
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *

class Check(Base):
    __tablename__ = 'check_tbl'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _check_serial = Column("check_serial", Integer, nullable=False)
    _price = Column("price", Integer)
    _national_id = Column("national_id", Integer, unique=True)
    _date_now = Column("date_now", Date)
    _date_end = Column("date_end", Date)

    _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    account = relationship("Account")

    def __init__(self, check_serial, price, national_id, date_now, date_end):
        self._check_serial = check_serial
        self._price = price
        self._national_id = national_id
        self._date_now = date_now
        self._date_end = date_end


    def get_id(self):
        return self._id

    def set_id(self):
        self._id = id

    def get_check_serial(self):
        return self._check_serial

    def set_check_serial(self,check_serial):
        self._check_serial = check_serial

    def get_price(self):
        return self._price

    def set_price(self,price):
        self._price = price

    def get_national_id(self):
        return self._national_id

    def set_national_id(self,national_id):
        self._national_id = national_id

    def get_date_now(self):
        return self._date_now

    def set_date_now(self, date_now):
        self._date_now = date_now

    def get_date_end(self):
        return self._date_end

    def set_date_end(self,date_end):
        self._date_end = date_end

    id = property(get_id,set_id)
    price = property(get_price,set_price)
    national_id = property(get_national_id,set_national_id)
    date_now = property(get_date_now,set_date_now)
    date_end = property(get_date_end,set_date_end)
