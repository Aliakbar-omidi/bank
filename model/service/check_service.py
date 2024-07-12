from controller.exceptions.exeptions import BankNotFoundError
from model.da.da import DataAccess
from model.entity import *


class CheckService:
    @staticmethod
    def save(check):
        check_da = DataAccess(Check)
        check_da.save(check)
        return check_da

    @staticmethod
    def edit(check):
        check_da = DataAccess(Check)
        if check_da.find_by_id(check.id):
            check_da.edit(check)
            return check_da
        else:
            raise BankNotFoundError()

    @staticmethod
    def remove(id):
        check_da = DataAccess(Check)
        if check_da.find_by_id(id):
            return check_da.remove(id)
        else:
            raise BankNotFoundError()

    @staticmethod
    def find_all():
        check_da = DataAccess(Check)
        return check_da.find_all()

    @staticmethod
    def find_by_id(id):
        check_da = DataAccess(Check)
        return check_da.find_by_id(id)

    @staticmethod
    def find_by_title(title):
        check_da = DataAccess(Check)
        return check_da.find_by(Check._title == title)
