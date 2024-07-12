from model.service import *
from model.entity import *
from model.tools.logger import Logger

class AccountController:
    @staticmethod
    def save_account(hesab_type, hesab_number):
        try:
            account = Account(hesab_type, hesab_number)
            AccountService.save(account)
            Logger.info(f"Account saved {account}")
            return True,account
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_account(hesab_type, hesab_number):
        try:
            account = Account(hesab_type, hesab_number)
            AccountService.edit(account)
            Logger.info(f"Account edited {account}")
            return True,account
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove_account(id):
        try:
            account = AccountService.remove(id)
            Logger.info(f"Account removed {account}")
            return True,account
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            account_list = AccountService.find_all()
            Logger.info(f"Job FindAll")
            return True,account_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"