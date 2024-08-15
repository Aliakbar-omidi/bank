from model.entity import *


class Card(Base):
    __tablename__ = "card_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _number_card = Column("number_card", Integer, nullable=False)
    _cvv2 = Column("cvv2", Integer, nullable=False)
    _expiration_date = Column("expiration_date", Date, nullable=False)
    _password = Column("password", String(20), nullable=False)

    _account_id = Column("account_id", Integer, ForeignKey("account_tbl.id"))
    account = relationship("Account")

    def __init__(self, number_card, cvv2, expiration_date, password):
        self.id = None
        self.number_card = number_card
        self.cvv2 = cvv2
        self.expiration_date = expiration_date
        self.password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def number_card(self):
        return self._number_card

    @number_card.setter
    def number_card(self, number_card):
        self._number_card = number_card

    @property
    def cvv2(self):
        return self._cvv2

    @cvv2.setter
    def cvv2(self, cvv2):
        self._cvv2 = cvv2

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self._expiration_date = expiration_date

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id
