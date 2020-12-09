from tkinter import *
from tkinter import ttk
from Center import CenterPage
from PreRecord import Prerecord
from Medicien import MedicienClass
import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from patientDetails """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()

class Patient:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.y = 20
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        Label(self.root, text="Patient Page").place(x=290, y=self.y)
        patient = dict()
        for i in PatientList:
            if i[0] == self.id:
                patient = i
        x = 30
        Label(self.root, text="Name: " + patient[1]).place(x=x, y=self.y + 40)
        Label(self.root, text="Patient ID: " + patient[0]).place(x=x, y=self.y + 65)
        Label(self.root, text="Blood Group: " + patient[2]).place(x=x, y=self.y + 90)
        Label(self.root, text="Phone: " + patient[3]).place(x=x, y=self.y + 115)
        Label(self.root, text="Height: " + patient[4]).place(x=x, y=self.y + 140)
        Label(self.root, text="Weight: " + str(patient[5]) + " kg").place(x=x, y=self.y + 165)
        Label(self.root, text="Current address: " + patient[6]).place(x=x, y=self.y + 190)
        Label(self.root, text="Parmanent address: " + patient[7]).place(x=x, y=self.y + 215)
        ttk.Button(self.root, text="Pre Record",
                   command=self.preRecord
                   ).place(x=x+170, y=self.y + 300)
        ttk.Button(self.root, text="Medicine",
                   command=self.medicine
                   ).place(x=x + 330, y=self.y + 300)

    def preRecord(self):
        self.root.destroy()
        Prerecord(self.id)

    def medicine(self):
        self.root.destroy()
        MedicienClass(self.id)

# This will be comment
#Patient("192-65442")

