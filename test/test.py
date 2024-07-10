from model.da.da import DataAccess
from model.entity.account import Account
from model.entity.person import Person
from model.entity.check import Check
from model.entity.transaction import Transaction
from model.entity.card import Card

# account = Account("asssa", 233332)
# account_da = DataAccess(Account)
# account_da.save(account)
# print(account.id)

# todo: در فایل دیتا بیس هم فقط فیلد ایدی ساخته میشود
# person = Person("ali", "mod",2123232332 ,2000/10/10, 32333323,"test@gmail.com")
# person_da = DataAccess(Person)
# person_da.save(person)
# print(person.id)


# todo: ارور دارد
check = Check(3434, 44344, 434444343, 200/12/10, 2000/12/12)
check_data = DataAccess(Check)
check_data.save(check)
print(check.id)
