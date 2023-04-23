import random
from tkinter import *

window = Tk()
window.title("Number guessing game")
label5 = Label(window, text="enter easy or hard")
label5.pack()
entry1 = Entry(window)
entry1.pack()
chance = 0


def chanc():
    global chance
    if (entry1.get() == "hard"):
        label = Label(window, text=f"im thinking of number in between 1 and 100, you have 5 chances")
        label.pack()
        chance = 6
        game()
    elif (entry1.get() == "easy"):
        label = Label(window, text=f"im thinking of number in between 1 and 100, you have 10 chances")
        label.pack()
        chance = 11
        game()


button2 = Button(window, text="enter", command=chanc)
button2.pack()
num = random.randint(1, 100)


def game():
    global chance
    entry = Entry(window)
    entry.pack()

    def check():
        global num
        if (num == int(entry.get())):
            label2 = Label(window, text="you got it right!")
            label2.pack()
        elif (int(entry.get()) > num):
            label3 = Label(window, text="too high ")
            label3.pack()
            game()
        else:
            label4 = Label(window, text="too low")
            label4.pack()
            game()

    button = Button(window, text="enter", command=check)
    button.pack()
    chance = chance - 1
    if (chance == 0):
        label6=Label(window,text="you ran out of choices")
        label6.pack()


window.mainloop()