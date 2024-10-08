from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class TransactionView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, transaction_list = TransactionController.find_all()
        if status:
            for transaction in transaction_list:
                self.table.insert("", END, values=(
                    transaction.id, transaction.serial, transaction.description, transaction.date_transaction,
                    transaction.time_transaction, transaction.payment_gateway, transaction.price, transaction.status,
                    transaction.account_id))

    def save_click(self):
        status_value = str(self.status._variable.get())
        status_bool = True if status_value == "True" else False
        status, result = TransactionController.save_transaction(self.serial._variable.get(),
                                                                self.description._variable.get(),
                                                                self.date_transaction._variable.get(),
                                                                self.time_transaction._variable.get(),
                                                                self.payment_gateway._variable.get(),
                                                                self.price._variable.get(), status_bool,
                                                                self.account_id._variable.get())
        if status:
            entered_data = (
                f"serial: {self.serial._variable.get()}\n"
                f"description: {self.description._variable.get()}\n"
                f"date: {self.date_transaction._variable.get()}\n"
                f"time: {self.time_transaction._variable.get()}\n"
                f"payment gateway: {self.payment_gateway._variable.get()}\n"
                f"price: {self.price._variable.get()}\n"
                f"status: {status_bool}\n"
                f"account id: {self.account_id._variable.get()}"
            )
            msg.showinfo("Save", f"transaction saved? \n {entered_data}")
            print(status_bool)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def b_edit_transaction(self):
        get_id = self.id._variable.get()
        find_id = TransactionController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Edit",
                         f"آیدی {get_id} پیدا شد حالا میتوانید فیلدهارا ادیت کنید و در نهایت دکمه ی Edit رو بزنید.")
            self.edit_button.place(x=100, y=380)
            self.s_button.place_forget()
            self.table.place(x=335, y=20)
            self.win.geometry("1230x425")
            self.serial.set_variable(find_id.serial)
            self.description.set_variable(find_id.description)
            self.date_transaction.set_variable(find_id.date_transaction)
            self.time_transaction.set_variable(find_id.time_transaction)
            self.payment_gateway.set_variable(find_id.payment_gateway)
            self.price.set_variable(find_id.price)
            self.status.set_variable(find_id.status)
            self.account_id.set_variable(find_id.account_id)
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def edit_transaction(self):
        status_value = self.status._variable.get()
        status_bool = True if status_value == "True" else False
        result = TransactionController.edit_transaction(self.id._variable.get(), self.serial._variable.get(),
                                                        self.description._variable.get(),
                                                        self.date_transaction._variable.get(),
                                                        self.time_transaction._variable.get(),
                                                        self.payment_gateway._variable.get(),
                                                        self.price._variable.get(), status_bool,
                                                        self.account_id._variable.get())
        if result:
            entered_data = (
                f"ID: {self.id._variable.get()}\n"
                f"serial: {self.serial._variable.get()}\n"
                f"description: {self.description._variable.get()}\n"
                f"date: {self.date_transaction._variable.get()}\n"
                f"time: {self.time_transaction._variable.get()}\n"
                f"payment gateway: {self.payment_gateway._variable.get()}\n"
                f"price: {self.price._variable.get()}\n"
                f"status: {status_bool}\n"
                f"account id: {self.account_id._variable.get()}"
            )
            msg.showinfo("edit", f"transaction edited? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_transaction(self):
        get_id = self.remove_row._variable.get()
        find_id = TransactionController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"TransactionId {get_id} delete?")
            TransactionController.remove_transaction(get_id)
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
        self.win.title("transaction View")
        self.win.geometry("1300x425")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20, distance=115)

        self.serial = TextWithLabel(self.win, "serial: ", 20, 60, distance=115)

        self.description = TextWithLabel(self.win, "description: ", 20, 100, distance=115)

        self.date_transaction = TextWithLabel(self.win, "date: ", 20, 140, distance=115)

        self.time_transaction = TextWithLabel(self.win, "time: ", 20, 180, distance=115)

        self.payment_gateway = TextWithLabel(self.win, "payment gateway: ", 20, 220, distance=115)

        self.price = TextWithLabel(self.win, "price: ", 20, 260, distance=115)

        self.status = TextWithLabel(self.win, "status: ", 20, 300, distance=115)

        self.account_id = TextWithLabel(self.win, "account id: ", 20, 340, distance=115)

        self.find_account = TextWithLabel(self.win, "Find Account By Id: ", 360, 260, distance=165)

        self.remove_row = TextWithLabel(self.win, "Remove Transaction By Id: ", 360, 300, distance=165)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=380)

        self.s_button = Button(self.win, text="Search", command=self.b_edit_transaction)
        self.s_button.place(x=325, y=20)

        self.edit_button = Button(self.win, text="edit", command=self.edit_transaction)

        Button(self.win, text="Search", command=self.find_account_by_id).place(x=730, y=260)

        Button(self.win, text="remove", command=self.remove_transaction).place(x=730, y=300)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings")

        self.table.column(1, width=75)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)
        self.table.column(9, width=75)

        self.table.heading(1, text="id")
        self.table.heading(2, text="serial")
        self.table.heading(3, text="description")
        self.table.heading(4, text="date")
        self.table.heading(5, text="time")
        self.table.heading(6, text="payment gateway")
        self.table.heading(7, text="price")
        self.table.heading(8, text="status")
        self.table.heading(9, text="account id")

        self.table.place(x=405, y=20)

        self.reset_form()

        self.win.mainloop()
