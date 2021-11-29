import tkinter
from PIL import Image, ImageTk


def createMode():
    pass


def challengeMode():
    pass


top = tkinter.Tk()
top.geometry("1024x648")
top.title('anydraw')
top.configure(bg='white')
logo = ImageTk.PhotoImage(Image.open("./logo.png"))
tkinter.Label(top, image=logo, borderwidth=0).pack()
tkinter.Button(top, text="创造模式", height=10,
               width=20, command=createMode).pack()
tkinter.Button(top, text="挑战模式", height=10,
               width=20, command=challengeMode).pack()
top.mainloop()
