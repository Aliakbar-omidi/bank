from model.service import *
from model.entity import *
from model.tools.decorators import exception_handling
from model.tools.logger import Logger


class AccountController:
    @staticmethod
    @exception_handling
    def save_account(hesab_type, hesab_number, person_id, bank_id):
        account = Account(hesab_type, hesab_number)
        account.person_id = person_id
        account.bank_id = bank_id
        AccountService.save(account)
        Logger.info(f"Account saved {account}")
        return True,account

    @staticmethod
    @exception_handling
    def edit_account(id, hesab_type, hesab_number,person_id, bank_id):
        account = Account(hesab_type, hesab_number)
        account.id = id
        account.person_id = person_id
        account.bank_id = bank_id
        AccountService.edit(account)
        Logger.info(f"Account edited {account}")
        return True, account

    @staticmethod
    @exception_handling
    def remove_account(id):
        account = AccountService.remove(id)
        Logger.info(f"Account removed {account}")
        return True,account

    @staticmethod
    def find_all():
        account_list = AccountService.find_all()
        Logger.info(f"Account FindAll")
        return True, account_list

    @staticmethod
    def find_by_id(id):
        return AccountService.find_by_id(id)