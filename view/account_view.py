from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from model.entity import *
from view import CardView
from view.check_view import CheckView
from view.transaction_view import TransactionView
from view.component.label_text import TextWithLabel


class AccountView:

    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, account_list = AccountController.find_all()
        if status:
            for account in account_list:
                self.table.insert("", END,
                                  values=(account.id, account.hesab_type, account.hesab_number, account.person_id,
                                          account.bank_id))

    def save_click(self):
        status, result = AccountController.save_account(self.hesab_type._variable.get(),
                                                        self.hesab_number._variable.get(),
                                                        self.person_id._variable.get(), self.bank_id._variable.get())
        if status:
            entered_data = (
                f"hesab type: {self.hesab_type._variable.get()}\n"
                f"hesab number: {self.hesab_number._variable.get()}\n"
                f"person id: {self.person_id._variable.get()}\n"
                f"bank id: {self.bank_id._variable.get()}\n"
            )
            msg.showinfo("Edit", f"Account saved? \n {entered_data}")
            msg.showinfo("after_save", f"  *تبریک می گوییم*\n حساب بانکی شماایجاد شد و حالا میتوانید برای کارت، جک و تراکنش حساب خودتان از دکمه های card و check و transaction استفاده کنید.")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_account(self):
        result = AccountController.edit_account(self.account_id._variable.get(), self.hesab_type._variable.get(),
                                                self.hesab_number._variable.get(), self.person_id._variable.get(),
                                                self.bank_id._variable.get())
        if result:
            entered_data = (
                f"Id: {self.account_id._variable.get()}\n"
                f"hesab type: {self.hesab_type._variable.get()}\n"
                f"hesab number: {self.hesab_number._variable.get()}\n"
                f"person id: {self.person_id._variable.get()}\n"
                f"bank id: {self.bank_id._variable.get()}\n"
            )
            msg.showinfo("Edit", f"AccountId {entered_data} edited? \n")
            self.reset_form()
        elif result.startswith("False"):
            msg.showerror("Error", result)

    def remove_account(self):
        get_id = self.remove_row._variable.get()
        find_id = AccountController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"AccountId {get_id} delete?")
            AccountController.remove_account(get_id)
            self.reset_form()
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def show_check(self):
        ui = CheckView()
        ui.show()

    def show_transaction(self):
        ui = TransactionView()
        ui.show()

    def show_card(self):
        ui = CardView()
        ui.show()

    def find_person_by_id(self):
        get_id = self.find_person._variable.get()
        find_id = PersonController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Find", f"PersonId {get_id} found")
        else:
            msg.showerror("Error", f"PersonId {get_id} not found")

    def find_bank_by_id(self):
        get_id = self.find_bank._variable.get()
        find_id = BankController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Find", f"BankId {get_id} found")
        else:
            msg.showerror("Error", f"BankId {get_id} not found")

    def show(self):
        self.win = Tk()
        self.win.title("account View")
        self.win.geometry("915x370")

        self.account_id = TextWithLabel(self.win, "Id For Edit : ", 20, 20)

        self.hesab_type = TextWithLabel(self.win, "hesab type: ", 20, 60)

        self.hesab_number = TextWithLabel(self.win, "hesab number: ", 20, 100)

        self.person_id = TextWithLabel(self.win, "person id: ", 20, 140)

        self.bank_id = TextWithLabel(self.win, "bank id: ", 20, 180)

        self.find_bank = TextWithLabel(self.win, "Find Bank By Id: ", 350, 240, distance=150)

        self.find_person = TextWithLabel(self.win, "Find Person By Id: ", 350, 280, distance=150)

        self.remove_row = TextWithLabel(self.win, "Remove Account By Id: ", 350, 320, distance=150)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=240)

        Button(self.win, text="Edit", command=self.edit_account).place(x=100, y=240)

        Button(self.win, text="card", command=self.show_card).place(x=20, y=280)

        Button(self.win, text="check", command=self.show_check).place(x=100, y=280)

        Button(self.win, text="transaction", command=self.show_transaction).place(x=180, y=280)

        Button(self.win, text="Search", command=self.find_bank_by_id).place(x=700, y=240)

        Button(self.win, text="Search", command=self.find_person_by_id).place(x=700, y=280)

        Button(self.win, text="Remove", command=self.remove_account).place(x=700, y=320)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5), show="headings")

        self.table.column(1, width=70)
        self.table.column(2, width=100)
        self.table.column(3, width=130)
        self.table.column(4, width=100)
        self.table.column(5, width=100)

        self.table.heading(1, text="account id")
        self.table.heading(2, text="hesab type")
        self.table.heading(3, text="hesab number")
        self.table.heading(4, text="person id")
        self.table.heading(5, text="bank id")

        self.table.place(x=350, y=20)

        self.reset_form()

        self.win.mainloop()
