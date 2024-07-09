from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Date
from model.entity import *
from sqlalchemy.orm import relationship
from model.tools.validator import *


class Card(Base):
    __tablename__ = "card_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _number_card = Column("number_card", Integer, nullable=False)
    _cvv2 = Column("cvv2",Integer, nullable=False)
    _expiration_date = Column("expiration_date", Date, nullable=False)
    _password = Column("password", String(20), nullable=False)

    _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    account = relationship("Account")

    def __init__(self, number_card, cvv2, expiration_date, password):
        self.id = None
        self.number_card = number_card
        self.cvv2 = cvv2
        self.expiration_date = expiration_date
        self.password = password

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

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