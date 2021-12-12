import tkinter as tk
from tkinter.constants import SEL_LAST
from PIL import Image, ImageTk


class createMode:
    def __init__(self, top):
        pass


def challengeMode():
    pass


class index:
    def __init__(self, top):
        global logo
        self.top = top
        frame1 = tk.Frame(top, relief=tk.RAISED, borderwidth=2)
        frame1.configure(bg='red')
        frame1.pack(side=tk.TOP, fill=tk.BOTH, ipadx=13, ipady=13, expand=0)
        frame2 = tk.Frame(top, relief=tk.RAISED, borderwidth=2)
        frame2.configure(bg='blue')
        frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, ipadx=13, ipady=13, expand=1)
        logo = ImageTk.PhotoImage(Image.open("./mmm/logo.png"))
        tk.Label(frame1, image=logo, borderwidth=0).pack()
        tk.Button(frame1, text="创造模式", height=5,
                  width=20, command=createMode(top)).pack()
        tk.Button(frame1, text="挑战模式", height=5,
                  width=20, command=challengeMode).pack()


top = tk.Tk()
top.geometry("1024x648")
top.title('anydraw')
top.configure(bg='white')
index(top)
top.mainloop()
