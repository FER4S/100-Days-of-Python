from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw
import time


def add_watermark():
    global final_img, template
    text_font = ImageFont.truetype('arial.ttf', 46)
    if is_pic.get() and is_text.get():
        text = entry_text.get()
        starting_img.paste(watermark, (0, 0))
        edit_img = ImageDraw.Draw(starting_img)
        edit_img.text((42, 0), text, 'yellow', text_font)
        final_img = edit_img
    elif is_pic.get():
        starting_img.paste(watermark, (0, 0))
        final_img = starting_img
    elif is_text.get():
        text = entry_text.get()
        edit_img = ImageDraw.Draw(starting_img)
        edit_img.text((0, 0), text, 'yellow', text_font)
        final_img = edit_img

    # print(f'{is_pic.get()=}, {is_text.get()=}')
    # time.sleep(3)
    template = ImageTk.PhotoImage(final_img)
    img.config(image=template)


def watermark_photo(wmrk):
    global watermark
    # starting_img = Image.open(original).resize((400, 400))
    watermark = Image.open(wmrk).resize((40, 40))

    # starting_img.paste(watermark, pos)
    #
    # template = ImageTk.PhotoImage(starting_img)
    # img.config(image=template)


def open_picture():
    global image2, original_path, starting_img
    original_path = fd.askopenfilename(title='Choose a Picture')
    starting_img = Image.open(original_path).resize((400, 400))
    # starting_img = starting_img.convert('RGB')
    image2 = ImageTk.PhotoImage(Image.open(original_path).resize((400, 400)))
    img.config(image=image2)
    img.image = image2


def get_wmrk():
    global wmrk
    path = fd.askopenfilename(title='Choose a Watermark')
    window.after(2000, watermark_photo, path)


def save_img():
    global final_img
    path = fd.asksaveasfilename(title='Save Picture', defaultextension='.png')
    final_img.save(path)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Image Watermarking')
window.config(padx=25, pady=25, bg='#35858B')
window.iconbitmap("icon.ico")

placeholder = ImageTk.PhotoImage(Image.open('placeholder-image.png').resize((400, 400)))

img = Label(window, image=placeholder)
img.image = placeholder
img.grid(row=0, column=2, rowspan=5)

is_pic = IntVar()
check_pic = Checkbutton(text='Picture Watermark', variable=is_pic, bg='#35858B')
check_pic.grid(row=1, column=0)

btn_photo = Button(window, text='Choose a Picture', command=open_picture, highlightthickness=0, padx=21, bg='#AEFEFF')
btn_photo.grid(row=0, column=0, padx=20)

btn_wmrk = Button(window, text='Choose a Watermark', command=get_wmrk, highlightthickness=0, padx=10, bg='#AEFEFF')
btn_wmrk.grid(row=2, column=0)

is_text = IntVar()
check_text = Checkbutton(text='Text Watermark', variable=is_text, bg='#35858B')
check_text.grid(row=3, column=0)

lbl_text = Label(text='Watermark Text:', bg='#35858B')
lbl_text.grid(row=4, column=0)

entry_text = Entry()
entry_text.grid(row=4, column=1, padx=10)

btn_add_wmrk = Button(text='Add Watermark', command=add_watermark, bg='#AEFEFF')
btn_add_wmrk.grid(row=6, column=0)

btn_save = Button(window, text='Save Picture', command=save_img, highlightthickness=0, bg='#AEFEFF')
btn_save.grid(row=6, column=2, pady=20)

window.mainloop()
