from model.service import *
from model.entity import *
from model.tools.decorators import exception_handling
from model.tools.logger import Logger


class BankController:
    @staticmethod
    def save_bank(name, location, start_time, end_time, branch, number_branch, status):
        try:
            bank = Bank(name, location, start_time, end_time, branch, number_branch, status)
            BankService.save(bank)
            Logger.info(f"bank saved {bank}")
            return True, bank
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_bank(id, name, location, start_time, end_time, branch, number_branch, status):
        try:
            bank = Bank(name, location, start_time, end_time, branch, number_branch, status)
            bank.id = id
            BankService.edit(bank)
            Logger.info(f"bank edited {bank}")
            return True, bank
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove_bank(id):
        try:
            bank = BankService.remove(id)
            Logger.info(f"bank removed {bank}")
            return True, bank
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            bank_list = BankService.find_all()
            Logger.info(f"Bank FindAll")
            return True, bank_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return BankService.find_by_id(id)
