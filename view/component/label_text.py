from tkinter import *


class TextWithLabel:
    def __init__(self, master, text,x,y,distance=100, disabled = False, data_type="str"):
        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.distance = distance
        self.variable = StringVar()

        match data_type:
            case "str":
                self._variable = StringVar()
            case "int":
                self._variable = IntVar()
            case "float":
                self._variable = DoubleVar()
            case "bool":
                self._variable = BooleanVar()

        Label(master, text=text).place(x=x, y=y)

        if disabled:
            self.text_box = Entry(master, textvariable=self.variable,state="readonly")
            self.text_box.place(x=x + distance, y=y)
        else:
            self.text_box = Entry(master, textvariable=self.variable)
            self.text_box.place(x=x + distance, y=y)