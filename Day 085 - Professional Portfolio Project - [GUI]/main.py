from tkinter import *
from random import shuffle

timer = None


def start():
    btn_start.config(state="disabled")
    with open('1-1000.txt') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))
        shuffle(data)
        data = data[:150]
    text = (' '.join(data))
    text_to_write.config(state=NORMAL)
    text_to_write.insert(INSERT, text)
    text_to_write.config(state=DISABLED)
    text_written.focus()
    count(60)


def count(sec):
    written = text_written.get(1.0, END).strip()
    compare_to = text_to_write.get(1.0, END)
    for i in range(len(written)):
        text_to_write.tag_remove('correct', f'1.{i}', f'1.{i + 1}')
        text_to_write.tag_remove('wrong', f'1.{i}', f'1.{i + 1}')
        if written[i] == compare_to[i]:
            text_to_write.tag_add('correct', f'1.{i}', f'1.{i + 1}')
        else:
            text_to_write.tag_add('wrong', f'1.{i}', f'1.{i + 1}')
    timer_min = sec // 60
    timer_sec = sec % 60
    lbl_timer.config(text=f'{timer_min:02}:{timer_sec:02}')
    if sec > 0:
        global timer
        timer = window.after(1000, count, sec-1)
    else:
        get_result()


def reset():
    btn_start.config(state="normal")
    window.after_cancel(timer)
    lbl_timer.config(text='')
    text_to_write.config(state=NORMAL)
    text_to_write.delete(1.0, END)
    text_to_write.config(state=DISABLED)
    text_written.config(state=NORMAL)
    text_written.delete(1.0, END)


def get_result():
    text_written.config(state=DISABLED)
    wpm = 0
    written = text_written.get(1.0, END).strip().split(' ')
    compare_to = text_to_write.get(1.0, END).split(' ')
    for i in range(len(written)):
        if written[i] == compare_to[i]:
            wpm += 1

    lbl_timer.config(text=f'Your WPM is {wpm}!! Great Job!💪')


window = Tk()
window.config(bg='#000', padx=80, pady=30)
window.title('Typing Speed Test')

lbl_title = Label(text='Welcome To My Typing Speed Test', bg='#000', fg='#fff', font=("Courier", 30, 'bold'))
lbl_title.grid(row=0, column=2)

lbl_timer = Label(text='', bg='#000', fg='#fff', font=("Courier", 16, 'bold'))
lbl_timer.grid(row=2, column=2)

text_to_write = Text(width=80, height=16, state=DISABLED, wrap=WORD)
text_to_write.tag_config("correct", foreground="green")
text_to_write.tag_config("wrong", foreground="red")
text_to_write.grid(row=1, column=0, columnspan=5)

text_written = Text(width=80, height=16, wrap=WORD)
text_written.grid(row=3, column=0, columnspan=5)

btn_start = Button(text='Start', command=start)
btn_start.grid(row=2, column=1, pady=10)

btn_reset = Button(text='Reset', command=reset)
btn_reset.grid(row=2, column=3, pady=10)

btn_exit = Button(text='Exit', command=window.destroy)
btn_exit.grid(row=4, column=2, pady=10)

window.mainloop()

