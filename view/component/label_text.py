from tkinter import *


class TextWithLabel:
    def __init__(self, master, text, x, y, distance=100, disabled=False):
        self.master = master
        self.text = text
        self.x = x
        self.y = y
        self.distance = distance
        self._variable = StringVar(master)

        Label(master, text=text).place(x=x, y=y)

        if disabled:
            self.text_box = Entry(master, textvariable=self._variable, state="readonly")
            self.text_box.place(x=x + distance, y=y)
        else:
            self.text_box = Entry(master, textvariable=self._variable)
            self.text_box.place(x=x + distance, y=y)