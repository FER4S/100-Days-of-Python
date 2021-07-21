from tkinter import *


def clicked():
    m = float(miles.get())
    km = m*1.609
    lbl3.config(text=km)


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

miles = Entry(width=5)
miles.focus()
miles.insert(END, string='0')
miles.grid(row=0, column=1)

lbl1 = Label(text='Miles')
lbl1.grid(row=0, column=2)

lbl2 = Label(text='is equal to')
lbl2.grid(row=1, column=0)

lbl3 = Label(text='0')
lbl3.grid(row=1, column=1)

lbl4 = Label(text='Km')
lbl4.grid(row=1, column=2)

btn = Button(text='Calculate', command=clicked)
btn.grid(row=2, column=1)

window.mainloop()
