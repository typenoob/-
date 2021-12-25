from PIL import ImageGrab


def save(window, canvas, filename):
    window.update()
    x = window.winfo_rootx()+canvas.winfo_x()
    y = window.winfo_rooty()+canvas.winfo_y()
    x1 = x+canvas.winfo_width()
    y1 = y+canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
