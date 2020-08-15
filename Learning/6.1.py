from tkinter import *

def ButtonClicked():
    image = Label(image=photo)
    image.pack()


window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('800x800')

photo = PhotoImage(file="hello.png")

lbl = Label(window, text="Best Image")

lbl.pack()

btn = Button(window, text="Click Me", command=ButtonClicked)

btn.pack()

window.mainloop()
