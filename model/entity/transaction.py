
from model.entity import *


class Transaction(Base):
    __tablename__ = 'transaction_tbl'
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _serial = Column("serial", Integer, nullable=False)
    _description = Column("description", String(30), nullable=False)
    _date_transaction = Column("date_transaction", Date, nullable=False)
    _time_transaction = Column("time_transaction", Time, nullable=False)
    _payment_gateway = Column("payment_gateway", String(30), nullable=False)
    _price = Column("price", Integer, default=0)
    _status = Column("status", Boolean)

    _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    account = relationship("Account")

    def __init__(self, serial, description, date_transaction, time_transaction, payment_gateway, price, status):
        self.id = None
        self.serial = serial
        self.description = description
        self.date_transaction = date_transaction
        self.time_transaction = time_transaction
        self.payment_gateway = payment_gateway
        self.price = price
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        self._serial = serial

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def date_transaction(self):
        return self._date_transaction

    @date_transaction.setter
    def date_transaction(self, date_transaction):
        self._date_transaction = date_transaction

    @property
    def time_transaction(self):
        return self._time_transaction

    @time_transaction.setter
    def time_transaction(self, time_transaction):
        self._time_transaction = time_transaction

    @property
    def payment_gateway(self):
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        self._payment_gateway = payment_gateway

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = boolean_validator(status, "Invalid status")

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id