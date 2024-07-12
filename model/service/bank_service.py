from controller.exceptions.exeptions import BankNotFoundError
from model.da.da import DataAccess
from model.entity import *


class BankService:
    @staticmethod
    def save(bank):
        bank_da = DataAccess(Bank)
        bank_da.save(bank)
        return bank_da

    @staticmethod
    def edit(bank):
        bank_da = DataAccess(Bank)
        if bank_da.find_by_id(bank.id):
            bank_da.edit(bank)
            return bank_da
        else:
            raise BankNotFoundError()

    @staticmethod
    def remove(id):
        bank_da = DataAccess(Bank)
        if bank_da.find_by_id(id):
            return bank_da.remove(id)
        else:
            raise BankNotFoundError()

    @staticmethod
    def find_all():
        bank_da = DataAccess(Bank)
        return bank_da.find_all()

    @staticmethod
    def find_by_id(id):
        bank_da = DataAccess(Bank)
        return bank_da.find_by_id(id)

    @staticmethod
    def find_by_title(title):
        bank_da = DataAccess(Bank)
        return bank_da.find_by(Bank._title == title)
