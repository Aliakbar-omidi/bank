from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    _shenase = Column("shenase",Integer, nullable=False)
    _description = Column("description",String(30), nullable=False)
    _payment_gateway = Column("payment_gateway",String(30), nullable=False)
    _price = Column("price",Integer, nullable=False)
    _status = Column("status",String(30), nullable=False)

    def __init__(self, shenase, description, payment_gateway, price, status):
        self.shenase = shenase
        self.description = description
        self.payment_gateway = payment_gateway
        self.price = price
        self.status = status

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_shenase(self):
        return self._shenase

    def set_shenase(self, shenase):
        self._shenase = shenase

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    id = property(get_id, set_id)
    shenase = property(get_shenase, set_shenase)
    description = property(get_description, set_description)