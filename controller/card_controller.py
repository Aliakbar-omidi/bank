from model.service import *
from model.entity import *
from model.tools.logger import Logger


class CardController:
    @staticmethod
    def save_card(number_card, cvv2, expiration_date, password, account_id):
        try:
            card = Card(number_card, cvv2, expiration_date, password)
            card.account_id = account_id
            CardService.save(card)
            Logger.info(f"card saved {card}")
            return True,card
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_card(id, number_card, cvv2, expiration_date, password, account_id):
        try:
            card = Card(number_card, cvv2, expiration_date, password)
            card.id = id
            card.account_id = account_id
            CardService.edit(card)
            Logger.info(f"card edited {card}")
            return True,card
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove_card(id):
        try:
            card = CardService.remove(id)
            Logger.info(f"card removed {card}")
            return True,card
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            card_list = CardService.find_all()
            Logger.info(f"Card FindAll")
            return True,card_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        return CardService.find_by_id(id)