from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class AccountView:
    def reset_form(self):
        status, account_list = AccountController.find_all()
        if status:
            for account in account_list:
                self.table.insert("", END,
                                  values=(account.hesab_type, account.hesab_number, account.person_id, account.bank_id))

    def save_click(self):
        status, result = AccountController.save_account(int(self.hesab_type.variable.get()),
                                                        int(self.hesab_number.variable.get()),
                                                        int(self.person_id.variable.get()),
                                                        int(self.bank_id.variable.get()))
        if status:
            msg.showinfo("account saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("account View")
        self.win.geometry("800x300")

        self.hesab_type = TextWithLabel(self.win, "hesab type: ", 20, 20)

        self.hesab_number = TextWithLabel(self.win, "hesab number: ", 20, 60)

        self.person_id = TextWithLabel(self.win, "person id: ", 20, 100)

        self.bank_id = TextWithLabel(self.win, "bank id: ", 20, 140)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=250)

        Button(self.win, text="Edit").place(x=100, y=250)

        Button(self.win, text="Remove").place(x=180, y=250)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)

        self.table.heading(1, text="hesab type")
        self.table.heading(2, text="hesab number")
        self.table.heading(3, text="person id")
        self.table.heading(4, text="bank id")

        self.table.place(x=320, y=20)

        self.reset_form()

        self.win.mainloop()
