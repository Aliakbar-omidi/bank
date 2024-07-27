
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
                self.table.insert("", END, values=(transaction.id, transaction.serial, transaction.description, transaction.date_time, transaction.payment_gateway, transaction.price, transaction.status, transaction.account_id))

    def save_click(self):
        status_value = self.status.variable.get()
        status_bool = True if status_value == "True" else False
        status, result = TransactionController.save_transaction(self.serial.variable.get(), self.description.variable.get(), self.date_time.variable.get(), self.payment_gateway.variable.get(), self.price.variable.get(), status_bool, self.account_id.variable.get())
        if status:
            msg.showinfo("transaction saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_transaction(self):
        status_value = self.status.variable.get()
        status_bool = True if status_value == "True" else False
        result = TransactionController.edit_transaction(self.id.variable.get(), self.serial.variable.get(), self.description.variable.get(), self.date_time.variable.get(), self.payment_gateway.variable.get(), self.price.variable.get(), status_bool, self.account_id.variable.get())
        if result:
            msg.showinfo("edit", "transaction edited?")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_transaction(self):
        get_id = self.remove_row.variable.get()
        TransactionController.remove_transaction(get_id)
        msg.showinfo("remove", "transaction removed!")
        self.reset_form()

    def show(self):
        self.win = Tk()
        self.win.title("transaction View")
        self.win.geometry("1200x400")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20, distance=115)

        self.serial = TextWithLabel(self.win, "serial: ", 20, 60, distance=115)

        self.description = TextWithLabel(self.win, "description: ", 20, 100, distance=115)

        self.date_time = TextWithLabel(self.win, "date time: ", 20, 140, distance=115)

        self.payment_gateway = TextWithLabel(self.win, "payment gateway: ", 20, 180, distance=115)

        self.price = TextWithLabel(self.win, "price: ", 20, 220, distance=115)

        self.status = TextWithLabel(self.win, "status: ", 20, 260, distance=115)

        self.account_id = TextWithLabel(self.win,"account id: ", 20, 300, distance=115)

        self.remove_row = TextWithLabel(self.win,"ID For Remove: ", 360, 260, distance=115)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        Button(self.win, text= "edit", command=self.edit_transaction).place(x=100 , y=340)

        Button(self.win, text= "remove", command=self.remove_transaction).place(x=680 ,  y=260)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=150)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)

        self.table.heading(1, text="id")
        self.table.heading(2, text="serial")
        self.table.heading(3, text="description")
        self.table.heading(4, text="date time")
        self.table.heading(5, text="payment gateway")
        self.table.heading(6, text="price")
        self.table.heading(7, text="status")
        self.table.heading(8, text="account id")

        self.table.place(x=335,y=20)

        self.reset_form()

        self.win.mainloop()

