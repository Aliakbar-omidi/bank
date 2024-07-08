from model.da.da import DataAccess
from model.entity.account import Account
from model.entity.person import Person
from model.entity.check import Check
from model.entity.transaction import Transaction
from model.entity.card import Card



account = Account("asssa", 233332)
account_da = DataAccess(Account)
account_da.save(account)
print(account.id)