from datetime import date
from model.da.da import DataAccess
from model.entity import *
from controller import *
from controller import *


# test ok --------------------------
# account = Account("test", 12121212)
# account_da = DataAccess(Account)
# account_da.save(account)
# print(account.id)

# test ok --------------------------
# bank = Bank("of","testi",'9:10:45','10:30:56',"ewewe",32323,False)
# bank_da = DataAccess(Bank)
# bank_da.save(bank)
# print(bank.id)

# test ok --------------------------
# card = Card(1221221,234, '2027/10/20', "asjhj22")
# card_da = DataAccess(Card)
# card_da.save(card)
# print(card_da.id)

# test ok --------------------------
# check = Check(233232,2332223,500002,'2021-01-01', '2021-01-05')
# check_data = DataAccess(Check)
# check_data.save(check)
# print(check.id)

# test ok --------------------------
# person = Person("test", "testpour",1234567, '2000/11/12', 91221122,"test_testi@gmail.com")
# person_da = DataAccess(Person)
# person_da.save(person)
# print(person.id)


# test controller bank ok ------------
# print(BankController.save_bank("mellat","teh",'08:20:30','10:20:30','rey',20,True))
# print(BankController.edit_bank(10,"edited","sd",'10:10:10','20:20:20',"teh",1234567,True))
# print(BankController.remove_bank(10))
# print(BankController.find_all())

# print(AccountController.save_account("jary",122554))
# print(AccountController.edit_account(5,'edited',545454))
# print(AccountController.remove_account(4))