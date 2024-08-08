from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class BankView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, bank_list = BankController.find_all()
        if status:
            for bank in bank_list:
                self.table.insert("", END, values=(bank.id, bank.name, bank.location, bank.start_time, bank.end_time, bank.branch, bank.number_branch, bank.status))

    def save_click(self):
        status_value = self.status._variable.get()
        status_bool = True if str(status_value) == "True" else False
        status, result = BankController.save_bank(self.name._variable.get(), self.location._variable.get(),self.start_time._variable.get(), self.end_time._variable.get(),self.branch._variable.get(), self.number_branch._variable.get(), status_bool)
        if status:
            entered_data = (
                f"Name: {self.name._variable.get()}\n"
                f"Location: {self.location._variable.get()}\n"
                f"Start_Time: {self.start_time._variable.get()}\n"
                f"End_Time: {self.end_time._variable.get()}\n"
                f"Branch: {self.branch._variable.get()}\n"
                f"Number_Branch: {self.number_branch._variable.get()}\n"
                f"status: {status_bool}\n"
            )
            msg.showinfo("Save", f"Bank saved? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_bank(self):
        status_value = self.status._variable.get()
        status_bool = True if status_value == "True" else False
        result = BankController.edit_bank(self.id._variable.get(), self.name._variable.get(), self.location._variable.get(), self.start_time._variable.get(), self.end_time._variable.get(), self.branch._variable.get(), self.number_branch._variable.get(), status_bool)
        if result:
            entered_data = (
                f"ID: {self.id._variable.get()}\n"
                f"Name: {self.name._variable.get()}\n"
                f"Location: {self.location._variable.get()}\n"
                f"Start Time: {self.start_time._variable.get()}\n"
                f"End Time: {self.end_time._variable.get()}\n"
                f"Branch: {self.branch._variable.get()}\n"
                f"Number Branch: {self.number_branch._variable.get()}\n"
                f"status: {status_bool}\n"
            )
            msg.showinfo("Edit", f"Bank edited? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_bank(self):
        get_id = self.remove_row._variable.get()
        BankController.remove_bank(get_id)
        msg.showinfo("Bank deleted!", f"BankId {get_id} delete?")
        self.reset_form()

    def show(self):
        self.win = Tk()
        self.win.title("Bank View")
        self.win.geometry("1100x450")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20)

        self.name = TextWithLabel(self.win, "Name: ", 20, 60)

        self.location = TextWithLabel(self.win, "Location: : ", 20, 100)

        self.start_time = TextWithLabel(self.win, "Start Time: ", 20, 140)

        self.end_time = TextWithLabel(self.win, "End Time: ", 20, 180)

        self.branch = TextWithLabel(self.win, "Branch: ", 20, 220)

        self.number_branch = TextWithLabel(self.win, "Number Branch: ", 20, 260)

        self.status = TextWithLabel(self.win, "Status: ", 20, 300)

        self.remove_row = TextWithLabel(self.win, "ID For Remove: ", 330, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=380)

        Button(self.win, text= "edit", command=self.edit_bank).place(x=100 , y=380)

        Button(self.win, text= "remove", command=self.remove_bank).place(x=630 , y=260)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)

        self.table.heading(1, text="id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Location")
        self.table.heading(4, text="Start Time")
        self.table.heading(5, text="End Time")
        self.table.heading(6, text="Branch")
        self.table.heading(7, text="Number Branch")
        self.table.heading(8, text="Status")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()