from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Center import CenterPage
import sqlite3
from jsonFileHandeler import jsonfilehandeler
from DoctorPage import Doctor

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from patient """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()

class Addrecord:
    entry_Problem = None
    entry_Date = None
    entry_Medicine = None
    entry_Note = None

    def __init__(self, id, doctorid):
        self.doctorid = doctorid
        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        x = 50
        y = 5
        Label(self.root, text="Add record").place(x=290, y=y+15)
        for i in PatientList:
            if i[0] == self.id:
                self.name = i[1]

        Label(self.root, text="Name: " + self.name).place(x=x, y=y + 55)
        Label(self.root, text="Problem title").place(x=x, y=y + 90)
        self.entry_Problem = ttk.Entry(self.root, width=30)
        self.entry_Problem.place(x=x+90, y=y + 90)
        Label(self.root, text="Date").place(x=x, y=y + 130)
        self.entry_Date = ttk.Entry(self.root, width=30)
        self.entry_Date.place(x=x+90, y=y + 130)
        Label(self.root, text="Medicine").place(x=x, y=y + 170)
        self.entry_Medicine = Text(self.root, height=4, width=40)
        self.entry_Medicine.place(x=x + 90, y=y + 170)
        Label(self.root, text="Note").place(x=300, y=y + 250)
        self.entry_Note = Text(self.root, height=5, width=60)
        self.entry_Note.place(x=x + 20, y=y + 280)
        ttk.Button(self.root, text="Add",
                   command=self.add_details
                   ).place(x=280, y=y + 390)

    def add_details(self):
        record = dict()
        record["DesName"] = self.entry_Problem.get()
        record["Date"] = self.entry_Date.get()
        record["Medicine"] = self.entry_Medicine.get("1.0", END)
        record["note"] = self.entry_Note.get("1.0", END)
        jsonfilehandeler(record, self.id, self. name)
        self.root.destroy()
        Doctor(self.doctorid)



Addrecord("192-65441")