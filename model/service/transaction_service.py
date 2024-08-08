from controller.exceptions.exeptions import BankNotFoundError
from model.da.da import DataAccess
from model.entity import *


class TransactionService:
    @staticmethod
    def save(transaction):
        transaction_da = DataAccess(Transaction)
        transaction_da.save(transaction)
        return transaction_da

    @staticmethod
    def edit(transaction):
        transaction_da = DataAccess(Transaction)
        if transaction_da.find_by_id(transaction.id):
            transaction_da.edit(transaction)
            return transaction_da
        else:
            raise BankNotFoundError()

    @staticmethod
    def remove(id):
        transaction_da = DataAccess(Transaction)
        if transaction_da.find_by_id(id):
            return transaction_da.remove(id)
        else:
            raise BankNotFoundError()

    @staticmethod
    def find_all():
        transaction_da = DataAccess(Transaction)
        return transaction_da.find_all()

    @staticmethod
    def find_by_id(id):
        transaction_da = DataAccess(Transaction)
        return transaction_da.find_by_id(id)
