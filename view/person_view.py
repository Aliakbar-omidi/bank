
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class PersonView:
    def reset_form(self):
        status, person_list = PersonController.find_all()
        if status:
            for person in person_list:
                self.table.insert("", END, values=(person.name, person.family, person.national_id, person.birthday, person.phone, person.email))

    def save_click(self):
        status, result = PersonController.save_person(self.name.get(), self.family.get(), self.national_id.get(), self.birthday.get(),self.phone.get(),self.email.get())
        if status:
            msg.showinfo("person saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("person View")
        self.win.geometry("1100x400")

        name = TextWithLabel(self.win, "name: ", 20, 20)

        family = TextWithLabel(self.win, "family: ", 20, 60)

        national_id = TextWithLabel(self.win, "national id: ", 20, 100)

        birthday = TextWithLabel(self.win, "birthday: ", 20, 140)

        phone = TextWithLabel(self.win, "phone: ", 20, 180)

        email = TextWithLabel(self.win, "email: ", 20, 220)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=120)


        self.table.heading(1, text="name")
        self.table.heading(2, text="family")
        self.table.heading(3, text="national id")
        self.table.heading(4, text="birthday")
        self.table.heading(5, text="phone")
        self.table.heading(6, text="email")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()