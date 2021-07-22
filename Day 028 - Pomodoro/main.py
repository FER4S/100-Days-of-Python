from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = '✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    btnStart.config(state="normal")
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    lbl_timer.config(text='Timer', fg=GREEN)
    lbl_tick.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    btnStart.config(state="disabled")
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2:
        lbl_timer.config(text='WORK', fg=GREEN)
        count(work_sec)
    else:
        if reps == 8:
            lbl_timer.config(text='LONG BREAK', fg=RED)
            count(long_break_sec)
        else:
            lbl_timer.config(text='SHORT BREAK', fg=PINK)
            count(short_break_sec)
    lbl_tick.config(text=(reps // 2) * TICK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count(n):
    timer_min = n // 60
    timer_sec = n % 60

    canvas.itemconfig(timer_text, text=f'{timer_min:02}:{timer_sec:02}')
    if n > 0:
        global timer
        timer = window.after(1000, count, n-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

pic = PhotoImage(file='tomato.png')
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=pic)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

lbl_timer = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
lbl_timer.grid(row=0, column=1)

lbl_tick = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10))
lbl_tick.grid(row=3, column=1)

btnStart = Button(text='Start', command=start_timer)
btnStart.grid(row=2, column=0)

btnReset = Button(text='Reset', command=reset_timer)
btnReset.grid(row=2, column=2)
window.mainloop()
