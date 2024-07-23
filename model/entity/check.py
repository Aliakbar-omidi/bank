
from model.entity import *


class Check(Base):
    __tablename__ = 'check_tbl'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _check_serial = Column("check_serial", Integer)
    _price = Column("price", Integer)
    _date_now = Column("date_now", Date)
    _date_end = Column("date_end", Date)

    _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    account = relationship("Account")

    def __init__(self, check_serial, price, date_now, date_end):
        self.id = None
        self.check_serial = check_serial
        self.price = price
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

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id