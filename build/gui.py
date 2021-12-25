import tkinter as tk
from tkinter import Canvas
import gui_main
root = tk.Tk()
root.geometry("1440x1024")
root.configure(bg="#FFFFFF")
canvas = Canvas(
    root,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
gui_main.entry(canvas, root)
root.resizable(False, False)
root.mainloop()
