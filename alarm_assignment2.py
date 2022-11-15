from threading import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import datetime
import time
import winsound
from time import strftime
from datetime import datetime


class alarm:

    def __init__(self):
        self.pos = 0
        self.win = 0
        self.ent = 0
        self.lbl = 0
        self.arr1 = []
        self.arr2 = []
        self.arr3 = []
        self.dt = 0

    def layout(self):
        self.win = tk.Tk()
        self.win.geometry("400x460")
        self.win.title("Alarm Clock")

        self.dt = datetime.now()
        self.dt = self.dt.strftime('%A')
        print(self.dt)

        Label(self.win, text="Alarm Clock", font=(
            "Helvetica 20 bold"), fg="red").place(x=120, y=20)
        self.lbl = Label(self.win, font=('calibri', 20, 'bold'))
        self.lbl.place(x=128, y=60)
        self.time()

        self.listbox = Listbox(self.win, height=8, width=24,
                               bg="grey", activestyle='dotbox', font="Helvetica")
        self.listbox.place(x=64, y=200)
        btn1 = Button(self.win, text="Delete", command=self.delete_alarm)
        btn1.place(x=286, y=400)

        btn = Button(self.win, text="SET ALARM", command=self.set_alarm)
        btn.place(x=160, y=120)

        self.win.mainloop()

    def time(self):
        string = strftime('%I:%M:%S %p')
        self.lbl.config(text=string)
        for i in range(0, len(self.arr1)):
            if (string == self.arr1[i] and self.arr2[i] == self.dt):
                res = messagebox.askquestion(
                    'ALARM ALERT!!', 'Its '+self.arr1[i]+'!!'+'\nTime to Wake Up'+'\nWant to Snooze??')
                if (res == 'yes'):
                    if (self.arr3[i] < 3):
                        pos = self.arr1[i].find(':')
                        pos1 = int(self.arr1[i][pos+1:pos+3])
                        pos1 = pos1+5
                        pos2 = 0
                        if (pos1 >= 60):
                            pos1 = pos1-60
                            pos2 = 1+int(self.arr1[i][0:pos])

                        print(str(pos1)+" "+str(pos2))
                        str1 = 0
                        if (pos2 != 0):
                            str1 = str(pos2)+":"+str(pos1) + \
                                ":"+self.arr1[i][pos+4:]
                        else:
                            str1 = self.arr1[i][0:pos]+":" + \
                                str(pos1)+":"+self.arr1[i][pos+4:]

                        self.arr1[i] = str1
                        self.arr3[i] = self.arr3[i]+1
                        print(self.arr1)
                        messagebox.showinfo(
                            'Snoozed', 'Alarm will ring after 5 mins')
                    else:
                        messagebox.showinfo(
                            'SORRY', 'Sorry!! Already you have Snoozed the Alarm 3 times')

        self.lbl.after(1000, self.time)

    def set_alarm(self):
        timing = ('00', '01', '02', '03', '04', '05', '06', '07',
                  '08', '09', '10', '11', '12', '13', '14', '15',
                  '16', '17', '18', '19', '20', '21', '22', '23',
                  '24', '25', '26', '27', '28', '29', '30', '31',
                  '32', '33', '34', '35', '36', '37', '38', '39',
                  '40', '41', '42', '43', '44', '45', '46', '47',
                  '48', '49', '50', '51', '52', '53', '54', '55',
                  '56', '57', '58', '59', '60')
        days = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")

        frame = Toplevel(self.win)
        frame.geometry("436x300")
        frame.title("SET ALARM")
        Label(frame, text="Select Alarm", font=(
            "Helvetica 20 bold"), fg="red").place(x=120, y=12)

        label1 = Label(frame, text="Select the Day:: ",
                       font=("Helvetica 12")).place(x=116, y=92)
        self.day = StringVar(frame)
        self.day.set("DAY")
        self.days = OptionMenu(frame, self.day, *days)
        self.days.place(x=236, y=88)

        label2 = Label(frame, text="Select the Time:: ", font=("Helvetica 12"))
        label2.grid(row=0, column=0, padx=14, pady=132, sticky=W)
        self.hour = StringVar(frame)
        self.hour.set('HRS')
        self.hrs = OptionMenu(frame, self.hour, *timing[1:13])
        self.hrs.grid(row=0, column=1, sticky=W)

        self.minute = StringVar(frame)
        self.minute.set("MIN")
        self.mins = OptionMenu(frame, self.minute, *timing[0:60])
        self.mins.grid(row=0, column=2, sticky=W)

        self.second = StringVar(frame)
        self.second.set("SEC")
        self.secs = OptionMenu(frame, self.second, *timing[0:60])
        self.secs.grid(row=0, column=3, sticky=W)

        self.interval = StringVar(frame)
        self.interval.set("AM")
        self.intervals = OptionMenu(frame, self.interval, *("AM", "PM"))
        self.intervals.grid(row=0, column=4, sticky=W)

        btn = Button(frame, text="Set Alarm", font=(
            "Helvetica 15"), command=self.setting)
        btn.place(x=160, y=220)

    def setting(self):
        alarm_tm = self.hour.get()+":"+self.minute.get()+":" + \
            self.second.get()+" "+self.interval.get()
        self.listbox.insert(self.pos, alarm_tm+" "+self.day.get())
        self.pos = self.pos+1
        self.arr1.append(alarm_tm)
        self.arr2.append(self.day.get())
        self.arr3.append(0)
        print(self.arr1)
        print(self.arr2)

    def delete_alarm(self):
        string = 0
        pos = 0
        i = 0
        for j in self.listbox.curselection():
            string = self.listbox.get(i)
            i = j

        print(string)
        self.listbox.delete(i)

        for ele in range(0, len(self.arr1)):
            if (string == self.arr1[ele]+" "+self.arr2[ele]):
                pos = ele
                print(self.arr1[ele]+" "+self.arr2[ele])

        del self.arr1[i]
        del self.arr2[i]
        del self.arr3[i]
        print(self.arr1)

    # def alarm_check(self):
    #     string = strftime('%H:%M:%S %p')
    #     for i in range(0,len(self.arr1)):
    #         if(string==self.arr1[i]):
    #             messagebox.showinfo("Alarm", "Its Time")


ob = alarm()
ob.layout()
