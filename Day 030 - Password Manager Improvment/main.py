from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_list_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_list_numbers + password_list_symbols + password_list_letters
    shuffle(password_list)
    password = ''.join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_text = entry_website.get()
    email_text = entry_email.get()
    password_text = entry_password.get()
    full_data = {
        website_text: {
            'email': email_text,
            'password': password_text,
        }
    }

    if website_text and email_text and password_text:
        try:
            with open('data.json', 'r') as data:
                content = json.load(data)
        except:
            with open('data.json', 'w') as data:
                json.dump(full_data, data, indent=4)
        else:
            content.update(full_data)
            with open('data.json', 'w') as data:
                json.dump(content, data, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
    else:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")


# ---------------------------- SEARCH ------------------------------- #


def search():
    search_text = entry_website.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='There is no data yet!')
    else:
        try:
            messagebox.showinfo(title=search_text, message=f'Email: {data[search_text]["email"]}\n'
                                                           f'Password: {data[search_text]["password"]}')
        except KeyError:
            messagebox.showinfo(title='Error 404', message='The requested data was not found!')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='gray')

pic = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg='gray', highlightthickness=0)
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)

lbl_website = Label(text='Website:', bg='gray')
lbl_website.grid(row=1, column=0)

lbl_email = Label(text='Email/Username:', bg='gray')
lbl_email.grid(row=2, column=0)

lbl_password = Label(text='Password:', bg='gray')
lbl_password.grid(row=3, column=0)

entry_website = Entry(width=28)
entry_website.grid(row=1, column=1, ipadx=20)
entry_website.focus()

entry_email = Entry(width=53)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(END, string='example@gmail.com')

entry_password = Entry(width=28)
entry_password.grid(row=3, column=1, ipadx=20)

btn_generate = Button(text='Generate Password', command=generate_password)
btn_generate.grid(row=3, column=2)

btn_add = Button(text='Add', width=45, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

btn_search = Button(text='Search', command=search)
btn_search.grid(row=1, column=2, ipadx=32)

window.mainloop()
