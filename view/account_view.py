from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from model.da.da import DataAccess
from model.entity import *
from view.component.label_text import TextWithLabel


class AccountView:
    def __init__(self):
        self.Account = DataAccess(Account)

    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, account_list = AccountController.find_all()
        if status:
            for account in account_list:
                self.table.insert("", END,
                                  values=(account.id, account.hesab_type, account.hesab_number, account.person_id, account.bank_id))

    def save_click(self):
        status, result = AccountController.save_account(self.hesab_type._variable.get(), self.hesab_number._variable.get(), self.person_id._variable.get(), self.bank_id._variable.get())
        if status:
            msg.showinfo("Edit", f"Account saved? \n {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_account(self):
        result = AccountController.edit_account(self.account_id._variable.get(), self.hesab_type._variable.get(), self.hesab_number._variable.get(), self.person_id._variable.get(), self.bank_id._variable.get())
        if result:
            msg.showinfo("Edit", f"Account edited? \n {result}")
            self.reset_form()
        elif result.startswith("False"):
            msg.showerror("Error", result)

    def remove_account(self):
        get_id = self.remove_row._variable.get()
        AccountController.remove_account(get_id)
        msg.showinfo("Remove","Account removed?")
        self.reset_form()

    def show(self):
        self.win = Tk()
        self.win.title("account View")
        self.win.geometry("900x300")

        self.account_id = TextWithLabel(self.win, "Id For Edit : ", 20, 20)

        self.hesab_type = TextWithLabel(self.win, "hesab type: ", 20, 60)

        self.hesab_number = TextWithLabel(self.win, "hesab number: ", 20, 100)

        self.person_id = TextWithLabel(self.win, "person id: ", 20, 140)

        self.bank_id = TextWithLabel(self.win, "bank id: ", 20, 180)

        self.remove_row = TextWithLabel(self.win, "id for remove: ", 320, 240)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=240)

        Button(self.win, text="Edit", command=self.edit_account).place(x=100, y=240)

        Button(self.win, text="Remove", command=self.remove_account).place(x=620, y=240)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5), show="headings")

        self.table.column(1, width=70)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)

        self.table.heading(1, text="account id")
        self.table.heading(2, text="hesab type")
        self.table.heading(3, text="hesab number")
        self.table.heading(4, text="person id")
        self.table.heading(5, text="bank id")

        self.table.place(x=320, y=20)

        self.reset_form()

        self.win.mainloop()
