from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
words_dict = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_text, text=current_card["French"])
    canvas.itemconfig(canvas_image, image=front_img)

    # #Alternative method for picking words
    # # Access each key with its value
    # random_word = random.choice(words_dict)
    # language1 = list(random_word.keys())[0]
    # french_word = random_word[language1]
    # canvas.itemconfig(card_title, text=language1)
    # canvas.itemconfig(card_text, text=french_word)

    flip_timer = window.after(3500, func=flip_card)

def flip_card():
    #New card configurations
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text= "English")
    canvas.itemconfig(card_text, text=current_card["English"])

def remove_known_word():
    global words_dict
    words_already_known = pandas.DataFrame([current_card])
    words_already_known.to_csv('data/words_already_known.csv', mode='a', header=False, index=False)
    words_dict.remove(current_card)
    pandas.DataFrame(words_dict).to_csv('/home/dan/PycharmProjects/producti'
                                        'vity-projects/flash_card_app/data/french_words.csv', index=False)


    next_card()
# ------------------------------------ UI SETUP ------------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3500, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/card_front.png")
back_img = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image= front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


check_image = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=remove_known_word)
known_button.grid(column=1, row=1)

cross_image = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)


next_card()




window.mainloop()
