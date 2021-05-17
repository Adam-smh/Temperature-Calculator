from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Temperature Converter")
window.geometry("800x700")
window.config(bg="#A4161A")

fframe = Frame(window, width=250, height=150, relief="groove", borderwidth=2, bg="#A4161A")
fframe.place(relx="0.1", rely="0.1")

cf = Label(fframe, text="Celsius to Fahrenheit", bg="#A4161A", fg="#0B090A")
cf.place(relx="0.1", rely="0.1")

cf_entry = Entry(fframe, state="readonly")
cf_entry.place(relx="0.2", rely="0.6")

sframe = Frame(window, width=250, height=150, relief="groove", borderwidth=2, bg="#A4161A")
sframe.place(relx="0.6", rely="0.1")

fc = Label(sframe, text="Fahrenheit to Celsius", bg="#A4161A", fg="#0B090A")
fc.place(relx="0.1", rely="0.1")

fc_entry = Entry(sframe, state="readonly")
fc_entry.place(relx="0.2", rely="0.6")

cal_res = Label(window, width=30, height=5)
cal_res.place(relx="0.35", rely="0.65")


def ac():
    cf_entry.config(state="normal")
    fc_entry.delete(0, END)
    fc_entry.delete(0, END)
    if fc_entry.config(state="normal"):
        fc_entry.config(state="readonly")
    else:
        fc_entry.config(state="readonly")


acf = Button(window, text="Celsius to fahrenheit", command=ac)
acf.place(relx="0.21", rely="0.4")


def fc():
    fc_entry.config(state="normal")
    cf_entry.delete(0, END)
    cf_entry.delete(0, END)
    if cf_entry.config(state="normal"):
        cf_entry.config(state="readonly")
    else:
        cf_entry.config(state="readonly")


afc = Button(window, text="Fahrenheit to Celsius", command=fc)
afc.place(relx="0.6", rely="0.4")

close = Button(window, text='Exit', command='exit')
close.place(rely="0.75", relx="0.81")


def clear():
    fc_entry.delete(0, END)
    fc_entry.delete(0, END)
    fc_entry.config(state='readonly')
    cf_entry.delete(0, END)
    cf_entry.delete(0, END)
    cf_entry.config(state='readonly')
    cal_res.config(text="")


cdelete = Button(window, text="Clear", command=clear)
cdelete.place(relx="0.8", rely="0.65")


def calculate():
    try:
        if cf_entry["state"] == "normal":
            result = (int(cf_entry.get()) * 9 / 5 + 32)
            cal_res.config(text=result)
        elif fc_entry["state"] == "normal":
            result = (int(fc_entry.get()) - 32) * 5 / 9
            cal_res.config(text=result)
    except ValueError:
        messagebox.showerror(message="Enter Number")


cal = Button(window, text="Calculate", command=calculate)
cal.place(relx="0.1", rely="0.65")
mainloop()
