from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Center import CenterPage
from PreRecord import Prerecord
from AddRecord import Addrecord

import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from doctor where password='admin' """)
DoctorList = cursor.fetchall()
cursor.execute(""" select * from patient where password='admin' """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()


class Doctor:
    def __init__(self, id):
        self.entry_id = None
        self.entry_password = None

        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.y = 60
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        Label(self.root, text="Doctor Page").place(x=290, y=30)
        for i in DoctorList:
            if i[0] == self.id:
                self.name = i[1]
        Label(self.root, text="Name: " + self.name).place(x=30, y=self.y + 20)
        Label(self.root, text="Doctor Id: " + self.id).place(x=30, y=self.y + 50)

        Label(self.root, text="Patient ID").place(x=150, y=self.y + 130)
        self.entry_id = ttk.Entry(self.root, width=30)
        self.entry_id.place(x=230, y=self.y + 130)

        Label(self.root, text="Password").place(x=150, y=self.y + 170)
        self.entry_password = ttk.Entry(self.root, width=30, show="*")
        self.entry_password.place(x=230, y=self.y + 170)

        ttk.Button(self.root, text="Pre Record",
                   command=lambda: self.getIdPassword("pre")
                   ).place(x=210, y=self.y + 240)

        ttk.Button(self.root, text="Add Record",
                   command=lambda: self.getIdPassword("add")
                   ).place(x=330, y=self.y + 240)

    def getIdPassword(self, track):
        id = self.entry_id.get()
        password = self.entry_password.get()
        self.Authentication(id, password, track)

    def Authentication(self, id, password, track):
        id_first = id.split("-")
        if id_first[0] == "192":
            for i in PatientList:
                if i[0] == id and i[2] == password:
                    self.root.destroy()
                    if track == "pre":
                        Prerecord(id)
                    elif track == "add":
                        Addrecord(id, self.id)
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        else:
            messagebox.showinfo(title='Error', message="Id or Password is incorrect")
