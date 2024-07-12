from controller.exceptions.exeptions import BankNotFoundError
from model.da.da import DataAccess
from model.entity import *


class CardService:
    @staticmethod
    def save(card):
        card_da = DataAccess(Card)
        card_da.save(card)
        return card_da

    @staticmethod
    def edit(card):
        card_da = DataAccess(Card)
        if card_da.find_by_id(card.id):
            card_da.edit(card)
            return card_da
        else:
            raise BankNotFoundError()

    @staticmethod
    def remove(id):
        card_da = DataAccess(Card)
        if card_da.find_by_id(id):
            return card_da.remove(id)
        else:
            raise BankNotFoundError()

    @staticmethod
    def find_all():
        card_da = DataAccess(Card)
        return card_da.find_all()

    @staticmethod
    def find_by_id(id):
        card_da = DataAccess(Card)
        return card_da.find_by_id(id)

    @staticmethod
    def find_by_title(title):
        card_da = DataAccess(Card)
        return card_da.find_by(Card._title == title)
