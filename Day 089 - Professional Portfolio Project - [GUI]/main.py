from tkinter import *


timer = None
length = None


def callback(*args):
    if timer:
        window.after_cancel(timer)
    if len(text_written.get(1.0, END)) != 1:
        count(5)


def count(sec):
    global timer

    for tag in text_written.tag_names():
        text_written.tag_remove(tag, "1.0", "end")

    lbl_timer.config(text=f'Timer: {sec}', fg='#874356')

    if sec == 3:
        text_written.tag_add('green', '1.0', 'end')
    elif sec == 2:
        text_written.tag_add('yellow', '1.0', 'end')
    elif sec == 1:
        text_written.tag_add('red', '1.0', 'end')

    if sec > 0:
        timer = window.after(1000, count, sec-1)
    else:
        delete_text()


def delete_text():
    window.after_cancel(timer)
    lbl_timer.config(text='Your Text Has Been Deleted!', fg='red')
    text_written.delete(1.0, END)


window = Tk()
window.config(bg='#F6E7D8', padx=80, pady=30)
window.title('Disappearing Text Writing App')

lbl_title = Label(text='Disappearing Text Writing App', font=("Courier", 16, 'bold'), bg='#F6E7D8', fg='#874356')
lbl_title.grid(row=0, column=1, pady=10)


text_written = Text(width=80, height=20, wrap=WORD, padx=10, pady=10, bd=5)
text_written.tag_config('green', foreground='green')
text_written.tag_config('yellow', foreground='yellow')
text_written.tag_config('red', foreground='red')
text_written.bind('<KeyRelease>', callback)
text_written.grid(row=1, column=0, columnspan=3)

lbl_timer = Label(text='', font=("Courier", 16, 'bold'), bg='#F6E7D8', fg='#874356')
lbl_timer.grid(row=2, column=1, pady=10)


window.mainloop()

