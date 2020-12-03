from tkinter import *
from tkinter import ttk
DoctorList = [("191-45041", "Jasim"), ("191-45042", "karim"), ("191-45043", "Rahim"), ("191-4504", "Masum"), ("191-4505", "Jon")]
PatientList = [("192-65441", "Jakaria"), ("192-65442", "Hasan"), ("192-65443", "Roni"), ("192-65444", "Mannan"), ("192-65445", "Ajgor")]


class Patient:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.y = 20
        self.item()
        self.root.mainloop()

    def item(self):
        Label(self.root, text="-------Patient Page-------").place(x=250, y=self.y)
        for i in PatientList:
            if i[0] == self.id:
                self.name = i[1]
        Label(self.root, text="Welcome " + self.name).place(x=270, y=self.y + 20)

