from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class CheckView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, check_list = CheckController.find_all()
        if status:
            for check in check_list:
                self.table.insert("", END, values=(
                    check.id, check.check_serial, check.price, check.date_now, check.date_end, check.account_id))

    def save_click(self):
        status, result = CheckController.save_check(self.check_serial._variable.get(), self.price._variable.get(),
                                                    self.date_now._variable.get(), self.date_end._variable.get(),
                                                    self.account_id._variable.get())
        if status:
            entered_data = (
                f"Check Serial: {self.check_serial._variable.get()}\n"
                f"Price: {self.price._variable.get()}\n"
                f"Date Now: {self.date_now._variable.get()}\n"
                f"Date End: {self.date_end._variable.get()}\n"
                f"Account id: {self.account_id._variable.get()}"
            )
            msg.showinfo("Save", f"check saved? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_check(self):
        result = CheckController.edit_check(self.id._variable.get(), self.check_serial._variable.get(),
                                            self.price._variable.get(), self.date_now._variable.get(),
                                            self.date_end._variable.get(), self.account_id._variable.get())
        if result:
            entered_data = (
                f"ID: {self.id._variable.get()}\n"
                f"Check Serial: {self.check_serial._variable.get()}\n"
                f"Price: {self.price._variable.get()}\n"
                f"Date Now: {self.date_now._variable.get()}\n"
                f"Date End: {self.date_end._variable.get()}\n"
                f"Account id: {self.account_id._variable.get()}"
            )
            msg.showinfo("Edit", f"check edited? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_check(self):
        get_id = self.remove_row._variable.get()
        find_id = CardController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"AccountId {get_id} delete?")
            CardController.remove_card(get_id)
            self.reset_form()
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def find_account_by_id(self):
        get_id = self.find_account._variable.get()
        find_id = AccountController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Find", f"AccountId {get_id} found")
        else:
            msg.showerror("Error", f"AccountId {get_id} not found")

    def show(self):
        self.win = Tk()
        self.win.title("check View")
        self.win.geometry("1000x350")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20)

        self.check_serial = TextWithLabel(self.win, "number check: ", 20, 60)

        self.price = TextWithLabel(self.win, "Price: ", 20, 100)

        self.date_now = TextWithLabel(self.win, "Aate now: ", 20, 140)

        self.date_end = TextWithLabel(self.win, "Aate end: ", 20, 180)

        self.account_id = TextWithLabel(self.win, "Account id: ", 20, 220)

        self.find_account = TextWithLabel(self.win, "Find Account By Id: ", 350, 235, distance=133)

        self.remove_row = TextWithLabel(self.win, "Remove Check By Id: ", 350, 275, distance=133)

        Button(self.win, text="Save", command=self.save_click).place(x=20, y=275)

        Button(self.win, text="Edit", command=self.edit_check).place(x=100, y=275)

        Button(self.win, text="Search", command=self.find_account_by_id).place(x=675, y=235)

        Button(self.win, text="Remove", command=self.remove_check).place(x=675, y=275)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)

        self.table.heading(1, text="id")
        self.table.heading(2, text="check serial")
        self.table.heading(3, text="price")
        self.table.heading(4, text="date now")
        self.table.heading(5, text="date end")
        self.table.heading(6, text="account id")

        self.table.place(x=320, y=20)

        self.reset_form()

        self.win.mainloop()
