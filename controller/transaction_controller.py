from model.service import *
from model.entity import *
from model.tools.logger import Logger


class TransactionController:
    @staticmethod
    def save_transaction(transaction_serial, price, national_id, date_now, date_end):
        try:
            transaction = Transaction(transaction_serial, price, national_id, date_now, date_end)
            TransactionService.save(transaction)
            Logger.info(f"transaction saved {transaction}")
            return True,transaction
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_transaction(transaction_serial, price, national_id, date_now, date_end):
        try:
            transaction = Transaction(transaction_serial, price, national_id, date_now, date_end)
            TransactionService.edit(transaction)
            Logger.info(f"transaction edited {transaction}")
            return True,transaction
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove_transaction(id):
        try:
            transaction = TransactionService.remove(id)
            Logger.info(f"transaction removed {transaction}")
            return True,transaction
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            transaction_list = TransactionService.find_all()
            Logger.info(f"transaction FindAll")
            return True,transaction_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"