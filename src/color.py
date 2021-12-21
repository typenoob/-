
from tkinter.colorchooser import *
import tkinter as tk
from tkinter.simpledialog import *
fgcolor="black" #全局变量画笔颜色 默认为黑色

def color(f="black"):
    c = askcolor(color=f, title="选择画笔颜色")
    f = c[1]
    return f


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("1024x648")
    window.title('shape')
    window.configure(bg='white')
    canvas = tk.Canvas(window, width=1000, height=1000,
                       highlightthickness=0, bg='#AFEEEE')

    canvas.pack()




    window.mainloop()

