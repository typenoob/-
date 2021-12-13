def stopDraw(self, event):#停止绘画
    self.startDrawFlag = False
    self.lastDraw = 0


def startDraw(self, event):#开始绘画
    self.drawpad.delete(self.lastDraw)
    if not self.startDrawFlag:
        self.startDrawFlag = True
        self.x = event.x
        self.y = event.y


def mysave(self, event):#保存
    pass


def myyqt(self, event):#油漆桶
    pass


def myLine(self, event):#直线
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


def myLineArrow(self, event):#箭头直线
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


def myRect(self, event):#矩形
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


def myOval(self, event):#椭圆
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


def myPen(self, event):#画笔
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


def myErasor(self, event):#橡皮擦
    self.startDraw(event)
    self.drawpad.create_rectangle(event.x - 20, event.y - 20, event.x, event.y,
                                  outline=self.bgcolor,
                                  fill=self.bgcolor)
    self.x = event.x
    self.y = event.y


def message(self):#提示信息
    if self.v.get() == "粗细":
        messagebox.showwarning("未选择粗细", "请先选择粗细")