import tkinter as tk
from tkinter.simpledialog import *


class Eraser:
    def __init__(self,t):
        self.x = 0
        self.y = 0
        self.lastDraw = 0
        self.startDrawFlag = False
        self.t = t
    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def myEraser(self, event):
        if self.t == 1:
            self.startDraw(event)
            self.drawpad.create_rectangle(event.x - 25, event.y - 25, event.x, event.y,
                                          outline='white',
                                          fill='white')
            self.x = event.x
            self.y = event.y

        elif self.t == 2:
            self.startDraw(event)
            self.drawpad.create_rectangle(event.x - 50, event.y - 50, event.x, event.y,
                                          outline='white',
                                          fill='white')
            self.x = event.x
            self.y = event.y

    def bind(self, canvas):
        self.drawpad = canvas
        canvas.bind("<B1-Motion>", self.myEraser)
        canvas.bind("<ButtonRelease-1>", self.stopDraw)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("1024x648")
    window.title('shape')
    window.configure(bg='white')
    canvas = tk.Canvas(window, width=1000, height=1000,
                       highlightthickness=0, bg='#AFEEEE')
    canvas.pack()
    Eraser().bind(canvas)
    window.mainloop()