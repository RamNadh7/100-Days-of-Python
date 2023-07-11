from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data= pandas.read_csv("data/french_words.csv")
    data_dict=original_data.to_dict(orient="records")
else:
    data_dict=data.to_dict(orient="records")
random_card={}

def next_card():
    global random_card,flip_timer
    window.after_cancel(flip_timer)
    random_card= random.choice(data_dict)
    # print(random_card["French"])
    canvas.itemconfig(Title_Text,text="French",fill="black")
    canvas.itemconfig(Word_Text,text=random_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_img)
    flip_timer=window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(Title_Text,text="English",fill="white")
    canvas.itemconfig(Word_Text,text=random_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)


def know():
    data_dict.remove(random_card)
    next_card()
    data=pandas.DataFrame(data_dict)
    data.to_csv("data/to_learn.csv",index=False)

window=Tk()
window.title("Flash Cards App")
window.config(bg=BACKGROUND_COLOR,highlightthickness=0,padx=50,pady=50)

flip_timer=window.after(3000, func=flip_card)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_img=PhotoImage(file="./images/card_front.png")
card_back_img=PhotoImage(file="./images/card_back.png")

card_background=canvas.create_image(400,263,image=front_img)




Title_Text=canvas.create_text(400,180,text="Title",font=("Ariel",30,"italic"))
Word_Text=canvas.create_text(400,280,text="Word",font=("Ariel",50,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


wrong_image=PhotoImage(file="./images/wrong.png")
Wrong_Button=Button(image=wrong_image,highlightthickness=0,command=next_card)
Wrong_Button.grid(row=1,column=0)


right_image=PhotoImage(file="./images/right.png")
Right_Button=Button(image=right_image,highlightthickness=0,command=know)
Right_Button.grid(row=1,column=1)

next_card()


window.mainloop()