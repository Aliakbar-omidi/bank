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
                self.table.insert("", END, values=(
                    card.id, card.number_card, card.cvv2, card.expiration_date, card.password, card.account_id))

    def save_click(self):
        status, result = CardController.save_card(self.number_card._variable.get(), self.cvv2._variable.get(),
                                                  self.expiration_date._variable.get(), self.password._variable.get(),
                                                  self.account_id._variable.get())
        if status:
            entered_data = (
                f"Number card: {self.number_card._variable.get()}\n"
                f"Cvv2: {self.cvv2._variable.get()}\n"
                f"Expiration date: {self.expiration_date._variable.get()}\n"
                f"Password: {self.password._variable.get()}\n"
                f"Account id: {self.account_id._variable.get()}\n"
            )
            msg.showinfo("Save", f"card saved? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def b_edit_card(self):
        get_id = self.id._variable.get()
        find_id = CardController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Edit",
                         f"آیدی {get_id} پیدا شد حالا میتوانید فیلدهارا ادیت کنید و در نهایت دکمه ی Edit رو بزنید.")
            self.edit_button.place(x=100, y=280)
            self.s_button.place_forget()
            self.table.place(x=320, y=20)
            self.win.geometry("910x350")
            self.number_card.set_variable(find_id.number_card)
            self.cvv2.set_variable(find_id.cvv2)
            self.expiration_date.set_variable(find_id.expiration_date)
            self.password.set_variable(find_id.password)
            self.account_id.set_variable(find_id.account_id)
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def edit_card(self):
        result = CardController.edit_card(self.id._variable.get(), self.number_card._variable.get(),
                                          self.cvv2._variable.get(), self.expiration_date._variable.get(),
                                          self.password._variable.get(), self.account_id._variable.get())
        if result:
            entered_data = (
                f"Id: {self.id._variable.get()}\n"
                f"Number card: {self.number_card._variable.get()}\n"
                f"Cvv2: {self.cvv2._variable.get()}\n"
                f"Expiration date: {self.expiration_date._variable.get()}\n"
                f"Password: {self.password._variable.get()}\n"
                f"Account id: {self.account_id._variable.get()}\n"
            )
            msg.showinfo("Edit", f"card edited? {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_card(self):
        get_id = self.row_remove._variable.get()
        find_id = CardController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"CardId {get_id} delete?")
            CardController.remove_card(get_id)
            self.reset_form()
        else:
            msg.showerror("Error", f"cardId {get_id} not found")

    def find_account_by_id(self):
        get_id = self.find_account._variable.get()
        find_id = AccountController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Find", f"AccountId {get_id} found")
        else:
            msg.showerror("Error", f"AccountId {get_id} not found")

    def show(self):
        self.win = Tk()
        self.win.title("card View")
        self.win.geometry("970x350")

        self.id = TextWithLabel(self.win, "CardID For Edit: ", 20, 20)

        self.number_card = TextWithLabel(self.win, "number card: ", 20, 60)

        self.cvv2 = TextWithLabel(self.win, "cvv2: ", 20, 100)

        self.expiration_date = TextWithLabel(self.win, "expiration date: ", 20, 140)

        self.password = TextWithLabel(self.win, "password: ", 20, 180)

        self.account_id = TextWithLabel(self.win, "account id: ", 20, 220)

        self.find_account = TextWithLabel(self.win, "Find Account By Id: ", 330, 240, distance=125)

        self.row_remove = TextWithLabel(self.win, "Remove Card By Id: ", 330, 280, distance=125)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=280)

        self.s_button = Button(self.win, text="Search", command=self.b_edit_card)
        self.s_button.place(x=310, y=20)

        self.edit_button = Button(self.win, text="edit", command=self.edit_card)

        Button(self.win, text="Search", command=self.find_account_by_id).place(x=650, y=240)

        Button(self.win, text="remove", command=self.remove_card).place(x=650, y=280)

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

        self.table.place(x=390, y=20)

        self.reset_form()

        self.win.mainloop()
