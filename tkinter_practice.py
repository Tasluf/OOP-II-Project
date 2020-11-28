from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DoctorPage import Doctor

DoctorList = [("191-45041", "Jasim", "admin"), ("191-45042", "karim", "admin"), ("191-45043", "Rahim", "admin"), ("191-4504", "Masum", "admin"), ("191-4505", "Jon", "admin")]
PatientList = [("192-65441", "Jasim", "admin"), ("192-65442", "karim", "admin"), ("192-65443", "Rahim", "admin"), ("192-65444", "Masum", "admin"), ("192-65445", "Jon", "admin")]


class LoginPage:
    def __init__(self):
        y = 70
        self.root = Tk()
        self.root.geometry('640x480')
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
        self.root.mainloop()

    def getIdPassword(self):
        id = self.entry_id.get()
        password = self.entry_password.get()
        success = self.Authentication(id, password)

        if not success[0]:
            messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        else:
            self.root.destroy()
            Doctor(success[2])


    def Authentication(self, id, password):
        id_first = id.split("-")
        if id_first[0] == "191":
            for i in DoctorList:
                if i[0] == id and i[2] == password:
                    doc = "Doctor"
                    wel = i[1]
                    return [True, doc, wel]
            else:
                return [False]
        elif id_first[0] == "192":
            for i in PatientList:
                if i[0] == id and i[2] == password:
                    pan = "Patient"
                    wel = i[1]
                    return [True, pan, wel]
            else:
                return [False]
        else:
            return [False]


if __name__ == '__main__':
    LoginPage()

