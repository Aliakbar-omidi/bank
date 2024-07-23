
from model.entity import *


class Bank(Base):
    __tablename__ = "bank_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _location = Column("location", String(20), nullable=False)
    _start_time = Column("start_time", Time)
    _end_time = Column("end_time", Time)
    _branch = Column("branch", String(20))
    _number_branch = Column("number_branch", Integer)
    _status = Column("status", Boolean)

    account = relationship("Account",back_populates="bank")

    def __init__(self, name, location, start_time, end_time, branch, number_branch, status):
        self.id = None
        self.name = name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.branch = branch
        self.number_branch = number_branch
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name_validator(name, "Invalid name")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self,location):
        self._location = location

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, branch):
        self._branch = branch

    @property
    def number_branch(self):
        return self._number_branch

    @number_branch.setter
    def number_branch(self,number_branch):
        self._number_branch = number_branch

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = boolean_validator(status,"Invalid status")