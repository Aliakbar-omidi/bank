from controller.exceptions.exeptions import BankNotFoundError
from model.da.da import DataAccess
from model.entity import *


class AccountService:
    @staticmethod
    def save(account):
        account_da = DataAccess(Account)
        account_da.save(account)
        return account_da

    @staticmethod
    def edit(account):
        account_da = DataAccess(Account)
        if account_da.find_by_id(account.id):
            account_da.edit(account)
            return account_da
        else:
            raise BankNotFoundError()

    @staticmethod
    def remove(id):
        account_da = DataAccess(Account)
        if account_da.find_by_id(id):
            return account_da.remove(id)
        else:
            raise BankNotFoundError()

    @staticmethod
    def find_all():
        account_da = DataAccess(Account)
        return account_da.find_all()

    @staticmethod
    def find_by_id(id):
        account_da = DataAccess(Account)
        return account_da.find_by_id(id)

    @staticmethod
    def find_by_title(title):
        account_da = DataAccess(Account)
        return account_da.find_by(Account._title == title)
