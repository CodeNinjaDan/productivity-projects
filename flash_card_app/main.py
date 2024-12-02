from tkinter import *

import pandas
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"


words = pandas.read_csv("data/french_words.csv")
words_dict = words.to_dict(orient="records")
print(words_dict)

# ------------------------------------ UI SETUP ------------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/card_front.png")
canvas.create_image(400, 263, image= img)
start_text1 = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
start_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)










check_image = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/known.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(column=1, row=1)

cross_image = PhotoImage(file="/home/dan/PycharmProjects/productivity-projects/flash_card_app/images/unknown.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)













































window.mainloop()
