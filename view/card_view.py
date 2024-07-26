
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class CardView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, card_list = CardController.find_all()
        if status:
            for card in card_list:
                self.table.insert("", END, values=(card.id, card.number_card, card.cvv2, card.expiration_date, card.password, card.account_id))

    def save_click(self):
        status, result = CardController.save_card(self.number_card.variable.get(), self.cvv2.variable.get(), self.expiration_date.variable.get(), self.password.variable.get(),self.account_id.variable.get())
        if status:
            msg.showinfo("Save",f"card saved? \n {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_card(self):
        result = CardController.edit_card(self.id.variable.get(), self.number_card.variable.get(), self.cvv2.variable.get(), self.expiration_date.variable.get(), self.password.variable.get(),self.account_id.variable.get())
        if result:
            msg.showinfo("Edit", "card edited")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_card(self):
        get_id = self.row_remove.variable.get()
        CardController.remove_card(get_id)
        msg.showinfo("Remove", "card removed")
        self.reset_form()

    def show(self):
        self.win = Tk()
        self.win.title("card View")
        self.win.geometry("900x350")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20)

        self.number_card = TextWithLabel(self.win, "number card: ", 20, 60)

        self.cvv2 = TextWithLabel(self.win, "cvv2: ", 20, 100)

        self.expiration_date = TextWithLabel(self.win, "expiration date: ", 20, 140)

        self.password = TextWithLabel(self.win, "password: ", 20, 180)

        self.account_id = TextWithLabel(self.win, "account id: ", 20, 220)

        self.row_remove = TextWithLabel(self.win, "ID For Remove: ", 330, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=280)

        Button(self.win, text= "edit", command=self.edit_card).place(x=100 , y=280)

        Button(self.win, text= "remove", command=self.remove_card).place(x=630 , y=260)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6), show="headings")

        self.table.column(1, width=60)
        self.table.column(2, width=120)
        self.table.column(3, width=60)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)

        self.table.heading(1, text="ID")
        self.table.heading(2, text="Number_card")
        self.table.heading(3, text="Cvv2")
        self.table.heading(4, text="expiration date")
        self.table.heading(5, text="password")
        self.table.heading(6, text="account id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()
