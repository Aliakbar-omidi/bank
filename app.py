
from view import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class FrontView:

    def show_view_person(self):
        msg.showinfo("question", "برای ایجاد حساب بانکی ابتدا مشخصات خود را وارد کنید ")
        ui = PersonView()
        ui.show()

    def show_view_bank(self):
        ui = BankView()
        ui.show()

    def show(self):
        self.win = Tk()
        self.win.title("View")
        self.win.geometry("200x200")

        Button(self.win, text="ایجاد  حساب ", command=self.show_view_person).place(x=20, y=20)

        Button(self.win, text="بانک", command=self.show_view_bank).place(x=20, y=60)

        # self.table = ttk.Treeview(self.win, columns=(1,2), show="headings")

        # self.table.place(x=320, y=20)

        # self.reset_form()

        self.win.mainloop()


ui = BankView()
ui.show()