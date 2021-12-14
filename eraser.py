import tkinter as tk
from tkinter.simpledialog import *


class Eraser:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.lastDraw = 0
        self.startDrawFlag = False
        self.drawpad = canvas
        self.drawpad.pack()

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
        self.startDraw(event)
        self.drawpad.create_rectangle(event.x - 20, event.y - 20, event.x, event.y,
                                  outline='white',
                                  fill='white')
        self.x = event.x
        self.y = event.y

    def bind(self, canvas):
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
