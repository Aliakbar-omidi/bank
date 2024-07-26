
from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class PersonView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, person_list = PersonController.find_all()
        if status:
            for person in person_list:
                self.table.insert("", END, values=(person.id, person.name, person.family, person.national_id, person.birthdate, person.phone, person.email))

    def save_click(self):
        status, result = PersonController.save_person(self.name.variable.get(), self.family.variable.get(), self.national_id.variable.get(), self.birthdate.variable.get(),self.phone.variable.get(),self.email.variable.get())
        if status:
            msg.showinfo("person saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_person(self):
        result = PersonController.edit_person(self.id.variable.get(),self.name.variable.get(), self.family.variable.get(), self.national_id.variable.get(), self.birthdate.variable.get(),self.phone.variable.get(),self.email.variable.get())
        if result:
            msg.showinfo("Edit",f"person saved? {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("person View")
        self.win.geometry("1100x400")

        self.id = TextWithLabel(self.win, "ID For Remove: ", 20, 20)

        self.name = TextWithLabel(self.win, "name: ", 20, 60)

        self.family = TextWithLabel(self.win, "family: ", 20, 100)

        self.national_id = TextWithLabel(self.win, "national id: ", 20, 140)

        self.birthdate = TextWithLabel(self.win, "birthdate: ", 20, 180)

        self.phone = TextWithLabel(self.win, "phone: ", 20, 220)

        self.email = TextWithLabel(self.win, "email: ", 20, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        Button(self.win, text= "edit", command=self.edit_person).place(x=100 , y=340)

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

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()