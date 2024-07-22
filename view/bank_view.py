from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class BankView:
    def reset_form(self):
        status, bank_list = BankController.find_all()
        if status:
            for bank in bank_list:
                self.table.insert("", END, values=(bank.name, bank.location, bank.start_time, bank.end_time, bank.branch, bank.number_branch, bank.status))

    def save_click(self):
        status, result = BankController.save_bank(self.name.get(), self.location.get(), self.start_time.get(), self.end_time.get(), self.branch.get(), self.number_branch.get(), self.status.get())
        if status:
            msg.showinfo("Bank saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("Bank View")
        self.win.geometry("1100x400")

        name = TextWithLabel(self.win, "Name: ", 20, 20)

        location = TextWithLabel(self.win, "Location: : ", 20, 60)

        start_time = TextWithLabel(self.win, "Start Time: ", 20, 100)

        end_time = TextWithLabel(self.win, "End Time: ", 20, 140)

        branch = TextWithLabel(self.win, "Branch: ", 20, 180)

        number_branch = TextWithLabel(self.win, "Number Branch: ", 20, 220)

        status = TextWithLabel(self.win, "Status: ", 20, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6,7), show="headings")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)

        self.table.heading(1, text="Name")
        self.table.heading(2, text="Location")
        self.table.heading(3, text="Start Time")
        self.table.heading(4, text="End Time")
        self.table.heading(5, text="Branch")
        self.table.heading(6, text="Number Branch")
        self.table.heading(7, text="Status")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()