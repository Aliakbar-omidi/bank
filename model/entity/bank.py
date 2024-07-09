from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Time
from model.entity import *
from sqlalchemy.orm import relationship
from model.tools.validator import *
import re

class Bank(Base):
    __tablename__ = "bank_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("title", String(20), nullable=False)
    _location = Column("location", String(20),nullable=False)
    _start_work = Column("start_time", Time)
    _end_work = Column("end_time", Time)
    _branch = Column("branch", String(20), nullable=False)
    _number_branch = Column("number_branch",Integer)

    def __init__(self, name, location, start_work, end_work, branch,number_branch, status):
        self.id = None
        self.name = name
        self.location = location
        self.startwork = start_work
        self.end_work = end_work
        self.branch = branch
        self.number_branch = number_branch
        self.status = status

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_locatioon(self):
        return self._location

    def set_location(self,location):
        self._location = location

    def get_stert_work(self):
        return self._start_work

    def set_start_work(self,start_work):
        self._start_work = start_work

    def get_end_work(self):
        return self._end_work

    def set_end_work(self,end_work):
        self.end_work = end_work

    def get_branch(self):
        return self._branch

    def set_branch(self,branch):
        self._branch = branch

    def get_number_branch(self):
        return self._number_branch

    def set_number_branch(self,number_branch):
        self._number_branch = number_branch

    def get_status(self):
        return self._status

    def set_status(self, status):
        if isinstance(status,bool):
            self._status = status
        else:
            raise ValueError("status must be bool")

    id = property(get_id,set_id)
    name = property(get_name,set_name)
    location = property(get_locatioon,set_location)
    start_work = property(get_stert_work,set_start_work)
    end_work = property(get_end_work,set_end_work)