from tkinter import *
from tkinter import ttk


class Doctor:
    def __init__(self, name):
        self.name = name
        self.root = Tk()
        self.root.geometry('640x480')
        self.y = 20
        self.item()
        self.root.mainloop()

    def item(self):
        Label(self.root, text="-------Doctor Page-------").place(x=255, y=self.y)
        Label(self.root, text="Welcome " + self.name).place(x=270, y=self.y + 20)
