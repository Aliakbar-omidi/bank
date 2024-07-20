from model.da.da import DataAccess
from model.entity import *
from controller import *
from controller import *


# test controller bank ok ------------
# print(BankController.save_bank("mellat","teh",'08:20:30','10:20:30','rey',20,True))
# print(BankController.edit_bank(10,"edited","sd",'10:10:10','20:20:20',"teh",1234567,True))
# print(BankController.remove_bank(10))
# print(BankController.find_all())

# test controller account ok ------------
# print(AccountController.save_account("jary",122554))
# print(AccountController.edit_account(5,'edited',545454))
# print(AccountController.remove_account(4))
print(AccountController.find_all())

# test controller card ok ------------
# print(CardController.save_card(12213323, 234,'2000-01-01',"21qwq")) #--
# print(CardController.remove_card(8))
# print(CardController.edit_card(7,90,90,'2010-10-10',"g62"))
# print(CardController.find_all())  #--


# test controller check ok ------------
# print(CheckController.save_check(122133, 20000, 3525, '2001-01-01', '2010-20-21'))
# print(CheckController.edit_check(9, 6666, 3525, 3232,'2001-11-22','2002-10-20'))
# print(CheckController.remove_check(6))
# print(CheckController.find_all())


# test controller person ok ------------
# print(PersonController.save_person("jafar","tt",23444,'2000-01-20',91234567,"testi@gmail.com"))
# print(PersonController.edit_person(6,"ahmad","ahmadi",656565,'1990-10-12',999838383,"ahmad@gmail.com"))
# print(PersonController.remove_person(7))
# print(PersonController.find_all())


# test controller transaction ------------
# date = '2018-01-20'
# time = '12:00:00'
# print(TransactionController.save_transaction(89899,"kharid kala",f'{date} {time}',"atm",4000,True))
# print(TransactionController.edit_transaction(3,7878,"kharid kala",'2024-12-21',"poz",30000,False))
# print(TransactionController.remove_transaction(4))
# print(TransactionController.find_all()) #--