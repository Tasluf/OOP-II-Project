from tkinter import *
from tkinter import ttk
from Center import CenterPage
from jsonFileHandeler import jsonfilehandeler

PreRecordList = jsonfilehandeler.read_from_json()


class MedicineClass:
    def __init__(self, id):
        self.id = id
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.y = 20
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        if PreRecordList in None:
            Label(self.root, text="Patient Page").place(x=290, y=self.y)
            Label(self.root, text="No record is added").place(x=260, y=self.y + 30)
        else:
            record = dict()
            for i in PreRecordList:
                if i['ID'] == self.id:
                    record = i

            Label(self.root, text="Patient Page").place(x=290, y=self.y)
            Label(self.root, text=record["Name"]).place(x=300, y=self.y + 30)
            Label(self.root, text="Current Medicine").place(x=30, y=self.y + 60)
            medicienList = record["RecordList"][0]["Medicine"].split(',')
            gap = 90
            count = 1
            for i in medicienList:
                Label(self.root, text=str(count) + ") " + i).place(x=30, y=self.y + gap)
                count += 1
                gap += 30



