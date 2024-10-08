from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from view.component.label_text import TextWithLabel
from view.account_view import AccountView


class PersonView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, person_list = PersonController.find_all()
        if status:
            for person in person_list:
                self.table.insert("", END, values=(
                    person.id, person.name, person.family, person.national_id, person.birthdate, person.phone,
                    person.email))

    def save_click(self):
        status, result = PersonController.save_person(self.name._variable.get(), self.family._variable.get(),
                                                      self.national_id._variable.get(), self.birthdate._variable.get(),
                                                      self.phone._variable.get(), self.email._variable.get())
        if status:
            entered_data = (
                f"Name: {self.name._variable.get()}\n"
                f"Family: {self.family._variable.get()}\n"
                f"National ID: {self.national_id._variable.get()}\n"
                f"Birthdate: {self.birthdate._variable.get()}\n"
                f"Phone: {self.phone._variable.get()}\n"
                f"Email: {self.email._variable.get()}"
            )
            msg.showinfo("Save", f"Save Person? \n{entered_data}")
            msg.showinfo("question", "مشخصات شما سیو شد. برای ساخت حساب کار بری روی دکمه ی create account کلیک کنید.")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def b_edit_person(self):
        get_id = self.id._variable.get()
        find_id = PersonController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Edit",
                         f"آیدی {get_id} پیدا شد حالا میتوانید فیلدهارا ادیت کنید و در نهایت دکمه ی Edit رو بزنید.")
            self.edit_button.place(x=100, y=340)
            self.s_button.place_forget()
            self.table.place(x=335, y=20)
            self.win.geometry("1150x400")
            self.name.set_variable(find_id.name)
            self.family.set_variable(find_id.family)
            self.national_id.set_variable(find_id.national_id)
            self.birthdate.set_variable(find_id.birthdate)
            self.phone.set_variable(find_id.phone)
            self.email.set_variable(find_id.email)
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def edit_person(self):
        result = PersonController.edit_person(self.id._variable.get(), self.name._variable.get(),
                                              self.family._variable.get(), self.national_id._variable.get(),
                                              self.birthdate._variable.get(), self.phone._variable.get(),
                                              self.email._variable.get())
        if result:
            entered_data = (
                f"ID: {self.id._variable.get()}\n"
                f"Name: {self.name._variable.get()}\n"
                f"Family: {self.family._variable.get()}\n"
                f"National ID: {self.national_id._variable.get()}\n"
                f"Birthdate: {self.birthdate._variable.get()}\n"
                f"Phone: {self.phone._variable.get()}\n"
                f"Email: {self.email._variable.get()}"
            )
            msg.showinfo("Edit", f"edit person? \n {entered_data}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_person(self):
        get_id = self.remove_row._variable.get()
        find_id = PersonController.find_by_id(get_id)
        if find_id:
            msg.showinfo("Remove", f"PersonId {get_id} delete?")
            PersonController.remove_person(get_id)
            self.reset_form()
        else:
            msg.showerror("Error", f"ID {get_id} not found")

    def show_account(self):
        ui = AccountView()
        ui.show()

    def show(self):
        self.win = Tk()
        self.win.title("person View")
        self.win.geometry("1220x400")

        self.id = TextWithLabel(self.win, "PersonID For ٍEdit: ", 20, 20, distance=115)

        self.name = TextWithLabel(self.win, "name: ", 20, 60, distance=115)

        self.family = TextWithLabel(self.win, "family: ", 20, 100, distance=115)

        self.national_id = TextWithLabel(self.win, "national id: ", 20, 140, distance=115)

        self.birthdate = TextWithLabel(self.win, "birthdate: ", 20, 180, distance=115)

        self.phone = TextWithLabel(self.win, "phone: ", 20, 220, distance=115)

        self.email = TextWithLabel(self.win, "email: ", 20, 260, distance=115)

        self.remove_row = TextWithLabel(self.win, "ID For Remove:", 360, 260)

        Button(self.win, text="save", command=self.save_click).place(x=20, y=340)

        self.s_button = Button(self.win, text="Search", command=self.b_edit_person)
        self.s_button.place(x=325, y=20)

        self.edit_button = Button(self.win, text="edit", command=self.edit_person)

        Button(self.win, text="remove", command=self.remove_person).place(x=660, y=260)

        Button(self.win, text="create account", command=self.show_account).place(x=300, y=340)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=140)
        self.table.column(7, width=140)

        self.table.heading(1, text="id")
        self.table.heading(2, text="name")
        self.table.heading(3, text="family")
        self.table.heading(4, text="national id")
        self.table.heading(5, text="birthdate")
        self.table.heading(6, text="phone")
        self.table.heading(7, text="email")

        self.table.place(x=405, y=20)

        self.reset_form()

        self.win.mainloop()
