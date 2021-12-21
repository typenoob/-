import tkinter as tk
from tkinter.simpledialog import *


class Shape:
    def __init__(self, thick=3,f='black',fillf=''):
        self.thick = thick
        self.x = 0
        self.y = 0
        self.fgcolor = f
        self.fillf = fillf
        self.lastDraw = 0
        self.startDrawFlag = False

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def myLine(self, event):
        self.startDraw(event)  # 这个设置使得每次画线不会重复出现
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                                 fill=self.fgcolor, width=self.thick)

    def myLineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST,
                                                 fill=self.fgcolor, width=self.thick)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y,fill= self.fillf,
                                                      outline=self.fgcolor, width=self.thick)

    def myOval(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_oval(self.x, self.y, event.x, event.y,fill= self.fillf,
                                                 outline=self.fgcolor, width=self.thick)

    def bind(self, canvas, choice):
        self.drawpad=canvas
        if choice == 1:
            canvas.bind("<B1-Motion>", self.myLine)
        elif choice == 2:
            canvas.bind("<B1-Motion>", self.myLineArrow)
        elif choice == 3:
            canvas.bind("<B1-Motion>", self.myRect)
        elif choice == 4:
            canvas.bind("<B1-Motion>", self.myOval)
        canvas.bind("<ButtonRelease-1>", self.stopDraw)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("1024x648")
    window.title('shape')
    window.configure(bg='white')
    canvas = tk.Canvas(window, width=1000, height=1000,
                       highlightthickness=0, bg='#AFEEEE')
    canvas.pack()
    Shape(3).bind(canvas, 3)
    window.mainloop()