from controller.exceptions.exeptions import BankNotFoundError
from model.da.da import DataAccess
from model.entity import *


class PersonService:
    @staticmethod
    def save(person):
        person_da = DataAccess(Person)
        person_da.save(person)
        return person_da

    @staticmethod
    def edit(person):
        person_da = DataAccess(Person)
        if person_da.find_by_id(person.id):
            person_da.edit(person)
            return person_da
        else:
            raise BankNotFoundError()

    @staticmethod
    def remove(id):
        person_da = DataAccess(Person)
        if person_da.find_by_id(id):
            return person_da.remove(id)
        else:
            raise BankNotFoundError()

    @staticmethod
    def find_all():
        person_da = DataAccess(Person)
        return person_da.find_all()

    @staticmethod
    def find_by_id(id):
        person_da = DataAccess(Person)
        return person_da.find_by_id(id)
