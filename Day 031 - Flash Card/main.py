from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
EN = None
FR = None

# ---------------------------- READING DATA ------------------------------- #

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
data_dic = data.to_dict(orient="records")

# ---------------------------- NEW WORD ------------------------------- #


def known():
    global EN, FR
    new_word()
    known_word = {'French': FR, 'English': EN}
    data_dic.remove(known_word)
    df = pandas.DataFrame(data_dic)
    df.to_csv('data/words_to_learn.csv', index=False)


def en_word(word):
    canvas.itemconfig(bg_img, image=card_back)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word, fill='white')


def new_word():
    global flip_timer, EN, FR
    window.after_cancel(flip_timer)
    word = choice(data_dic)
    EN = word['English']
    FR = word['French']
    canvas.itemconfig(bg_img, image=card_front)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=FR, fill='black')
    flip_timer = window.after(3000, en_word, EN)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flashy')

card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_img = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text='test', fill='black', font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text='word', fill='black', font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

btn_right = Button(image=right, highlightthickness=0, bd=0, command=known)
btn_right.grid(row=1, column=0)

btn_wrong = Button(image=wrong, highlightthickness=0, bd=0, command=new_word)
btn_wrong.grid(row=1, column=1)

flip_timer = window.after(3000, en_word)
new_word()


window.mainloop()
