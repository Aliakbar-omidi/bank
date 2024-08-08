from model.service import *
from model.entity import *
from model.tools.logger import Logger
from model.tools.decorators import exception_handling


class PersonController:
    @staticmethod
    @exception_handling
    def save_person(name, family, national_id, birthdate, phone, email):
            person = Person(name, family, national_id, birthdate, phone, email)
            PersonService.save(person)
            Logger.info(f"person saved {person}")
            return True, person

    @staticmethod
    @exception_handling
    def remove_person(id):
        person = PersonService.remove(id)
        Logger.info(f"person removed {person}")
        return True, person

    @staticmethod
    @exception_handling
    def find_all():
        person_list = PersonService.find_all()
        Logger.info(f"person FindAll")
        return True, person_list

    @staticmethod
    @exception_handling
    def edit_person(id, name, family, national_id, birthdate, phone, email):
        person = Person(name, family, national_id, birthdate, phone, email)
        person.id = id
        PersonService.edit(person)
        Logger.info(f"person edited {person}")
        return True, person

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return PersonService.find_by_id(id)
