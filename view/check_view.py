
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class CheckView:
    def reset_form(self):
        status, check_list = CheckController.find_all()
        if status:
            for check in check_list:
                self.table.insert("", END, values=(check.check_serial, check.price, check.date_now, check.date_end, check.account_id))

    def save_click(self):
        status, result = CheckController.save_check(self.check_serial.get(), self.price.get(), self.date_now.get(),self.date_end.get(),self.account_id.get())
        if status:
            msg.showinfo("check saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("check View")
        self.win.geometry("1000x400")

        self.check_serial = TextWithLabel(self.win, "number check: ", 20, 20)

        self.price = TextWithLabel(self.win, "price: ", 20, 60)

        self.date_now = TextWithLabel(self.win, "date now: ", 20, 100)

        self.date_end = TextWithLabel(self.win, "date end: ", 20, 140)

        self.account_id = TextWithLabel(self.win, "account id: ", 20, 180)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=280)

        Button(self.win, text= "Edit").place(x=100 , y=280)

        Button(self.win, text= "Remove").place(x=180 , y=280)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)

        self.table.heading(1, text="check serial")
        self.table.heading(2, text="price")
        self.table.heading(3, text="date now")
        self.table.heading(4, text="date end")
        self.table.heading(5, text="account id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()
