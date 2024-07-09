from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity import *
from sqlalchemy.orm import relationship
from model.tools.validator import *

class Transaction(Base):
    __tablename__ = 'transaction_tbl'
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _serial = Column("serial", Integer, nullable=False)
    _description = Column("description", String(30), nullable=False)
    _date = Column("date",DateTime, nullable=False)
    _payment_gateway = Column("payment_gateway", String(30), nullable=False)
    _price = Column("price", Integer, default=0)
    _status = Column("status", Boolean)

    _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    account = relationship("Account")

    def __init__(self, serial, description, payment_gateway, price, status):
        self.id = None
        self.serial = serial
        self.description = description
        self.payment_gateway = payment_gateway
        self.price = price
        self.status = status

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_serial(self):
        return self._serial

    def set_serial(self, serial):
        self._serial = serial

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_payment_gateway(self):
        return self._payment_gateway

    def set_payment_gateway(self, payment_gateway):
        self._payment_gateway = payment_gateway

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price



    id = property(get_id, set_id)
    serial = property(get_serial, set_serial)
    description = property(get_description, set_description)
    date = property(get_date, set_date)
    payment_gateway = property(get_payment_gateway, set_payment_gateway)
    price = property(get_price, set_price)