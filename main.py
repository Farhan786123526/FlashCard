import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
flash_card_dict={}

try:
    data = pandas.read_csv("data/word to learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    flash_card_dict=original_data.to_dict(orient="records")
else:
    flash_card_dict = data.to_dict(orient="records")


def flash_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(flash_card_dict)
    canvas.itemconfig(canvas_title,text="French",fill="black")

    canvas.itemconfig(french_word,text=current_card["French"],fill="black")
    canvas.itemconfig(front,image=card_front)
    flip_timer=window.after(3000, func=flip_card)
    # print(current_card)

def flip_card():
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(french_word,text=current_card["English"],fill="white")
    canvas.itemconfig(front,image=card_back)
def is_known():
    flash_card_dict.remove(current_card)
    flash_card()
    data=pandas.DataFrame(flash_card_dict)
    data.to_csv("data/word to learn.csv ",index=False)
    # print(len(flash_card_dict))


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)


canvas=Canvas(width=800 ,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
front=canvas.create_image(400,263,image=card_front)
canvas_title=canvas.create_text(400,150,font=("Ariel",42,"italic"),text="Title")
french_word=canvas.create_text(400,263,font=("Ariel",60,"bold"),text="Word")
canvas.grid(row=0,column=0,columnspan=2)

wrong_image=PhotoImage(file="images/wrong.png")
button_wrong=Button(image=wrong_image,highlightthickness=0,pady=20,padx=20,command=flash_card)
button_wrong.grid(column=0,row=1)

right_image=PhotoImage(file="images/right.png")
button_right=Button(image=right_image,highlightthickness=0,command=is_known)
button_right.grid(column=1,row=1)



flash_card()


window.mainloop()