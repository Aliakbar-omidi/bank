
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class AccountView:
    def reset_form(self):
        status, account_list = AccountController.find_all()  #hesab_type, hesab_number,person_id,bank_id
        if status:
            for account in account_list:
                self.table.insert("", END, values=(account.hesab_type, account.hesab_number, account.person_id, account.bank_id))

    def save_click(self):
        status, result = AccountController.save_account(self.hesab_type.get(), self.hesab_number.get(), self.person_id.get(), self.bank_id.get())
        if status:
            msg.showinfo("account saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("account View")
        self.win.geometry("1100x400")

        hesab_type = TextWithLabel(self.win, "hesab type: ", 20, 20)

        hesab_number = TextWithLabel(self.win, "hesab number: ", 20, 60)

        person_id = TextWithLabel(self.win, "person id: ", 20, 100)

        bank_id = TextWithLabel(self.win, "bank id: ", 20, 140)

        Button(self.win, text="save", command="save_click" ).place(x=20, y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)

        self.table.heading(1, text="hesab type")
        self.table.heading(2, text="hesab number")
        self.table.heading(3, text="person id")
        self.table.heading(4, text="bank id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()
