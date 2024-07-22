
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class TransactionView:
    def reset_form(self):
        status, transaction_list = TransactionController.find_all()
        if status:
            for transaction in transaction_list:
                self.table.insert("", END, values=(transaction.serial, transaction.description, transaction.date_time, transaction.payment_gateway, transaction.price, transaction.status,transaction.account_id))

    def save_click(self):
        status, result = TransactionController.save_transaction(self.serial.get(), self.description.get(), self.date_time.get(), self.payment_gateway.get(),self.price.get(),self.status.get(),self.account_id.get())
        if status:
            msg.showinfo("transaction saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("transaction View")
        self.win.geometry("1100x400")

        serial = TextWithLabel(self.win, "serial: ", 20, 20)

        description = TextWithLabel(self.win, "description: ", 20, 60)

        date_time = TextWithLabel(self.win, "date time: ", 20, 100)

        payment_gateway = TextWithLabel(self.win, "payment gateway: ", 20, 140)

        price = TextWithLabel(self.win, "price: ", 20, 180)

        status = TextWithLabel(self.win, "status: ", 20, 220)

        account_id = TextWithLabel(self.win,"account id: ", 20, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6,7), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)

        self.table.heading(1, text="serial")
        self.table.heading(2, text="description")
        self.table.heading(3, text="date time")
        self.table.heading(4, text="payment gateway")
        self.table.heading(5, text="price")
        self.table.heading(6, text="status")
        self.table.heading(7, text="account id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()