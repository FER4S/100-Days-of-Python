from tkinter import *
from tkinter import filedialog as fd
import pdfplumber
from gtts import gTTS


text = ''


def open_pdf():
    global text
    path = fd.askopenfilename(title='Choose a PDF file', filetypes=[("PDF files", ".pdf")])
    with pdfplumber.open(path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()


def save_audio():
    path = fd.asksaveasfilename(title='Save Audio', defaultextension='.mp3')
    obj = gTTS(text=text, lang='en', tld='co.uk')
    obj.save(path)


window = Tk()
window.config(padx=80, pady=30, bg='#8A39E1')
window.title('Text to Speech')

lbl_title = Label(text='PDF to Speech App', bg='#8A39E1', font=("Times", 25, 'bold'), fg='#ECC488')
lbl_title.grid(row=0, column=1)

btn_choose = Button(text='Choose a pdf file', command=open_pdf, bg='#ECC488')
btn_choose.grid(row=1, column=0, columnspan=3, pady=20)

btn_save = Button(text='Save Audio', command=save_audio, bg='#ECC488', padx=15)
btn_save.grid(row=2, column=0, columnspan=3)

window.mainloop()
