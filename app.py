from view import *
from tkinter import *
import tkinter.messagebox as msg


class FrontView:

    def show_view_person(self):
        msg.showinfo("question", "برای ایجاد حساب بانکی ابتدا مشخصات فردی خود را وارد کنید ")
        ui = PersonView()
        ui.show()

    def show_view_bank(self):
        ui = BankView()
        ui.show()

    def show_view_check(self):
        ui = CheckView()
        ui.show()

    def show_view_transaction(self):
        ui = TransactionView()
        ui.show()

    def show(self):
        self.win = Tk()
        self.win.title("View")
        self.win.geometry("630x200")

        frame1 = Frame(self.win, bd=2, relief="sunken")
        frame1.place(x=10, y=10, width=300, height=180)

        frame2 = Frame(self.win, bd=2, relief="sunken")
        frame2.place(x=320, y=10, width=300, height=180)

        Label(frame1, text="اگر حساب ندارید ابتدا مشخصات بانک و بعد \n حساب خود را ایجاد کتید.").pack()
        Button(frame1, text="بانک", command=self.show_view_bank).pack(pady=10)
        Button(frame1, text="ایجاد حساب", command=self.show_view_person).pack(pady=10)

        Label(frame2, text="در صورت داشتن حساب از موارد زیر استفاده کنید.").pack()
        Button(frame2, text="چک", command=self.show_view_check).pack(pady=10)
        Button(frame2, text="ایجاد تراکنش", command=self.show_view_transaction).pack(pady=10)

        self.win.mainloop()


ui = FrontView()
ui.show()
