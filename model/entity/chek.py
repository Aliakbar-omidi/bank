from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *

class Chek(Base):
    __tablename__ = 'che_tblk'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _shenase = Column("shenase", Integer, nullable=False)
    _price = Column("price", Integer)
    _national_id = Column("national_id", Integer, unique=True)
    _date_now = Column("date_now", DateTime)
    _date_end = Column("date_end", DateTime)


    def __init__(self, shenase, _price, national_id, date_now, date_end):
        self._shenase = shenase
        self._price = _price
        self._national_id = national_id
        self._date_now = date_now
        self._date_end = date_end

    def get_id(self):
        return self._id

    def set_id(self):
        self._id = str(self._id)

    def get_shenase(self):
        return self._shenase

    def set_shenase(self,shenase):
        self._shenase = shenase

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

    def set_date_now(self,date_now):
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
