from model.service import *
from model.entity import *
from model.tools.logger import Logger


class PersonController:
    @staticmethod
    def save_person(name, family, national_id, birthday, phone, email):
        try:
            person = Person(name, family, national_id, birthday, phone, email)
            PersonService.save(person)
            Logger.info(f"person saved {person}")
            return True,person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_person(id, name, family, national_id, birthday, phone, email):
        try:
            person = Person(name, family, national_id, birthday, phone, email)
            person.id = id
            PersonService.edit(person)
            Logger.info(f"person edited {person}")
            return True,person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove_person(id):
        try:
            person = PersonService.remove(id)
            Logger.info(f"person removed {person}")
            return True,person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            person_list = PersonService.find_all()
            Logger.info(f"person FindAll")
            return True,person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"