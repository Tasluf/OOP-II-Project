from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DoctorPage import Doctor
from PatientPage import Patient
from Center import CenterPage
import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from doctor where password='admin' """)
DoctorList = cursor.fetchall()
cursor.execute(""" select * from patient where password='admin' """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()


class LoginPage:
    def __init__(self):
        y = 70
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)

        Label(self.root, text="Login Page").place(x=280, y=y)
        Label(self.root, text="ID").place(x=170, y=y+30)
        self.entry_id = ttk.Entry(self.root, width=30)
        self.entry_id.place(x=200, y=y+30)
        Label(self.root, text="Password").place(x=120, y=y+60)
        self.entry_password = ttk.Entry(self.root, width=30, show="*")
        self.entry_password.place(x=200, y=y+60)
        ttk.Button(self.root, text="Login",
                            command=self.getIdPassword
                            ).place(x=280, y=y+100)

        CenterPage(self.root)
        self.root.mainloop()


    def getIdPassword(self):
        id = self.entry_id.get()
        password = self.entry_password.get()
        self.Authentication(id, password)

    def Authentication(self, id, password):
        id_first = id.split("-")
        if id_first[0] == "191":
            for i in DoctorList:
                if i[0] == id and i[2] == password:
                    self.root.destroy()
                    Doctor(id)
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        elif id_first[0] == "192":
            for i in PatientList:
                if i[0] == id and i[2] == password:
                    self.root.destroy()
                    Patient(id)
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        else:
            messagebox.showinfo(title='Error', message="Id or Password is incorrect")


if __name__ == '__main__':
    LoginPage()

