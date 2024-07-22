
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class CardView:
    def reset_form(self):
        status, card_list = CardController.find_all()
        if status:
            for card in card_list:
                self.table.insert("", END, values=(card.number_card, card.cvv2, card.expiration_date, card.password,card.account_id))

    def save_click(self):
        status, result = CardController.save_card(self.number_card.get(), self.cvv2.get(), self.expiration_date.get(), self.password.get(),self.account_id.get())
        if status:
            msg.showinfo("card saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("card View")
        self.win.geometry("1100x400")

        number_card = TextWithLabel(self.win, "number card: ", 20, 20)

        cvv2 = TextWithLabel(self.win, "cvv2: ", 20, 60)

        expiration_date = TextWithLabel(self.win, "expiration date: ", 20, 100)

        password = TextWithLabel(self.win, "password: ", 20, 140)

        account_id = TextWithLabel(self.win, "account id: ", 20, 180)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=60)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)

        self.table.heading(1, text="Number_card")
        self.table.heading(2, text="Cvv2")
        self.table.heading(3, text="expiration date")
        self.table.heading(4, text="password")
        self.table.heading(5, text="account id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()