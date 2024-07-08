from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from model.entity.base import Base
from sqlalchemy.orm import relationship
from model.tools.validator import *
import re

class Chek(Base):
    __tablename__ = 'chek'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _shenase = Column("shenase", Integer, nullable=False)
    _price = Column("price", Integer, nullable=False)
    _national_id = Column("national_id", Integer, nullable=False)
    _date_now = Column("date_now", DateTime, nullable=False)
    _date_end = Column("date_end", DateTime, nullable=False)


