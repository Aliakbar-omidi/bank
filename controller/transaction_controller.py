from model.service import *
from model.entity import *
from model.tools.logger import Logger


class TransactionController:
    @staticmethod
    def save_transaction(serial, description, date_transaction, time_transaction, payment_gateway, price, status,account_id):
        try:
            transaction = Transaction(serial, description, date_transaction, time_transaction, payment_gateway, price, status)
            transaction.account_id = account_id
            TransactionService.save(transaction)
            Logger.info(f"transaction saved {transaction}")
            return True,transaction
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_transaction(id, serial, description, date_transaction, time_transaction, payment_gateway, price, status, account_id):
        try:
            transaction = Transaction(serial, description, date_transaction, time_transaction, payment_gateway, price, status)
            transaction.id = id
            transaction.account_id = account_id
            TransactionService.edit(transaction)
            Logger.info(f"transaction edited {transaction}")
            return True, transaction
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

    @staticmethod
    def find_by_id(id):
        return TransactionService.find_by_id(id)