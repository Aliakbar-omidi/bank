from model.service import *
from model.entity import *
from model.tools.logger import Logger


class CheckController:
    @staticmethod
    def save_check(check_serial, price, national_id, date_now, date_end):
        try:
            check = Check(check_serial, price, national_id, date_now, date_end)
            CheckService.save(check)
            Logger.info(f"check saved {check}")
            return True,check
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit_check(check_serial, price, national_id, date_now, date_end):
        try:
            check = Check(check_serial, price, national_id, date_now, date_end)
            CheckService.edit(check)
            Logger.info(f"check edited {check}")
            return True,check
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove_check(id):
        try:
            check = CheckService.remove(id)
            Logger.info(f"check removed {check}")
            return True,check
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            check_list = CheckService.find_all()
            Logger.info(f"Check FindAll")
            return True,check_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"