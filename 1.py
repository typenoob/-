from tkinter import *
import tkinter as tk
from tkinter.simpledialog import *
from tkinter.colorchooser import *

class DrawApp(Frame):
    """开发画图软件"""

    def __init__(self, master=None, bgcolor="white"):
        super().__init__(master)  # super 父类方法调用
        self.master = master
        #  self.v = StringVar(mywindow)  用于存储变量，方便后面获取笔号，画出不同粗细的图画
        self.v = StringVar(mywindow)
        #  设置背景颜色，背景色为白色
        self.bgcolor = bgcolor
        #  设置xy 的初始值
        self.x = 0
        self.y = 0
        # 设置默认前景色，也就是画笔的颜色
        self.fgcolor = "red"
        self.lastDraw = 0
        self.startDrawFlag = False
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        """创建新的组件"""
        # 创建一个绘图区域
        self.drawpad = Canvas(mywindow, width=win_width, height=win_height, bg=self.bgcolor)
        self.drawpad.pack()
        # 创建按钮
        btn_start = Button(mywindow, text="保存", width=10, name="save")
        btn_start.pack(side="left")
        self.v.set("粗细")
        btn_pen1 = OptionMenu(mywindow, self.v, "细", "中", "粗")
        btn_pen1.pack(side="left")
        btn_rect = Button(mywindow, text="矩形", width=10, name="rect")
        btn_rect.pack(side="left")
        btn_clear = Button(mywindow, text="清屏", width=10, name="clear")
        btn_clear.pack(side="left")
        btn_erasor = Button(mywindow, text="橡皮檫", width=10, name="erasor")
        btn_erasor.pack(side="left")
        btn_line = Button(mywindow, text="直线", width=10, name="line")
        btn_line.pack(side="left")
        btn_lineArrow = Button(mywindow, text="箭头直线", width=10, name="lineArrow")
        btn_lineArrow.pack(side="left")
        btn_color = Button(mywindow, text="颜色", width=10, name="color")
        btn_color.pack(side="left")
        btn_oval = Button(mywindow, text="椭圆", width=10, name="oval")
        btn_oval.pack(side="left")
        btn_Text = Button(mywindow, text="画笔", width=10, name="pen2")
        btn_Text.pack(side="left")
        btn_Text = Button(mywindow, text="油漆桶", width=10, name="yqt")
        btn_Text.pack(side="left")
        # 事件处理
        #  bind_class,它接受三个参数，第一个参数是类名，第二个参数是事件类型，第三个参数是相应的操作
        btn_pen1.bind_class("Button", "<Button-1>", self.eventManager)
        self.drawpad.bind("<ButtonRelease-1>", self.stopDraw)

    def eventManager(self, event):
    #  获取事件名字，根据事件名字判断操作类型
        name = event.widget.winfo_name()
        if name == "line":
        #  在画图之前，必须要选择粗细才能够开始，    self.message() 用来提示
        #  用bind 函数绑定不同的事件
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myLine)
        elif name == "lineArrow":
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myLineArrow)
        elif name == "rect":
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myRect)
        elif name == "pen2":
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myPen)
        elif name == "oval":
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myOval)
        elif name == "erasor":
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myErasor)
        elif name == "clear":
            self.drawpad.delete("all")
        elif name == "color":
            c = askcolor(color=self.fgcolor, title="选择画笔颜色")
            self.fgcolor = c[1]
        elif name == "yqt":
            self.message()
            self.drawpad.bind("<B1-Motion>", self.myyqt)
        elif name=='save':
            self.drawpad.bind("<B1-Motion>", self.mysave)


#  增加一个判断
    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def mysave(self, event):
        pass
    def myyqt(self,event):
        pass
    def myLine(self, event):
        if self.v.get() == "细":
            self.startDraw(event)  # 这个设置使得每次画线不会重复出现

            self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                                     fill=self.fgcolor, width=1)
        if self.v.get() == "中":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                                     fill=self.fgcolor, width=3)
        if self.v.get() == "粗":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                                     fill=self.fgcolor, width=5)
    def myLineArrow(self, event):
        if self.v.get() == "细":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST,
                                                     fill=self.fgcolor, width=1)
        if self.v.get() == "中":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST,
                                                     fill=self.fgcolor, width=3)
        if self.v.get() == "粗":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST,
                                                     fill=self.fgcolor, width=5)
    def myRect(self, event):
        if self.v.get() == "细":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y,
                                                          outline=self.fgcolor, width=1)
        if self.v.get() == "中":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y,
                                  outline=self.fgcolor, width=3)
        if self.v.get() == "粗":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y,
                                  outline=self.fgcolor, width=5)

    def myOval(self, event):
        if self.v.get() == "细":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_oval(self.x, self.y, event.x, event.y,
                                                          outline=self.fgcolor, width=1)

        if self.v.get() == "中":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_oval(self.x, self.y, event.x, event.y,
                                       outline=self.fgcolor, width=3)
        if self.v.get() == "粗":
            self.startDraw(event)
            self.lastDraw = self.drawpad.create_oval(self.x, self.y, event.x, event.y,
                                       outline=self.fgcolor, width=5)
    def myPen(self, event):
        if self.v.get() == "细":
            self.startDraw(event)
            self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                     fill=self.fgcolor, width=1)
            self.x = event.x
            self.y = event.y
        if self.v.get() == "中":
            self.startDraw(event)
            self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                     fill=self.fgcolor, width=3)
            self.x = event.x
            self.y = event.y
        if self.v.get() == "粗":
            self.startDraw(event)
            self.drawpad.create_line(self.x, self.y, event.x, event.y,
                                     fill=self.fgcolor, width=5)
            self.x = event.x
            self.y = event.y
    def myErasor(self, event):
            self.startDraw(event)
            self.drawpad.create_rectangle(event.x-20, event.y-20, event.x, event.y,outline=self.bgcolor,fill=self.bgcolor)
            self.x = event.x
            self.y = event.y
    def message(self):
        if self.v.get() == "粗细":
            messagebox.showwarning("未选择粗细", "请先选择粗细")


if __name__ == '__main__':
    mywindow = Tk()
    win_width = 900
    win_height = 500
    mywindow.geometry(str(win_width) + "x" + str(win_height + 50) + "+320+130")
    mywindow.title('画板')
    app = DrawApp(master=mywindow)
    mywindow.mainloop()
