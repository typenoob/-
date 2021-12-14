import tkinter as tk
import color
fgcolor="red"
class Pen:
    draw_point = ['', '']  # 用于储存拖拉鼠标时的点
    revoke = []  # 用于储存每次鼠标绘图操作的ID供撤销用[[...],[...],[...]]
    recover = []  # 用于储存每次鼠标绘图的点构成的列表供恢复
    clear = []  # 用于记录是否使用过清空，因为列表可变，支持全局修改，所以用列表记录

    def __init__(self, thick):
        self.thick = thick

    def paint(self, event):
        if not event:  # 松开鼠标左键时执行，清空记录点
            # [:]只改变draw_point指向的列表的内容，不是重新赋值一个新的列表所以修改值全局通用
            self.draw_point[:] = ['', '']
            return
        point = [event.x, event.y]  # 此次传递的点坐标
        if self.draw_point == ['', '']:  # 按下鼠标左键开始拖动时执行
            self.draw_point[:] = point  # 保存拖动的第一个点
            if len(self.revoke) < len(self.recover):
                self.recover[len(self.revoke):] = []  # 用于使用过撤销后再绘图，清除撤销点后的恢复数据
            self.clear[:] = []
            self.revoke.append([])  # 新建一个撤销记录列表
            self.recover.append([])  # 新建一个恢复记录列表
            self.recover[-1].extend(point)  # 在新建的恢复记录列表里记录第一个点
        else:
            self.revoke[-1].append(
                canvas.create_line(self.draw_point[0], self.draw_point[1], event.x, event.y, fill=fgcolor, width=self.thick,
                                   tags="line")
            )  # 绘制的线段并保存到撤销记录的末次列表
            self.draw_point[:] = point  # 保存拖动点，覆盖上一次
            self.recover[-1].extend(point)  # 保存此次传递的点坐标到恢复记录的末次列表

    def bind(self, canvas):
        canvas.bind("<B1-Motion>", self.paint)  # 设定拖动鼠标左键画线段
        canvas.bind("<ButtonRelease-1>", lambda event: self.paint(0))

    def re(self, rev=0, rec=0):
        if rev and self.revoke:  # 撤销执行
            for i in self.revoke.pop(-1):
                canvas.delete(i)  # pop弹出最后一个撤销列表，删除图像
            # 恢复执行，恢复列表需要大于撤销列表
        elif rec and self.recover and (len(self.revoke) != len(self.recover)):
            if self.clear:
                for i in self.recover:
                    self.revoke.append(
                        [canvas.create_line(i, fill="#476042", width=self.thick, tags="line")])
                self.clear[:] = []
            else:
                self.revoke.append([canvas.create_line(
                    self.recover[len(self.revoke)], fill="#476042", width=self.thick, tags="line")])
        # 清空功能

    def clr(self):
        canvas.delete("line")  # 清除 tags = "line"的图像
        self.revoke[:] = []
        self.clear.append(1)



if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("1024x648")
    window.title('pen')
    window.configure(bg='white')
    canvas = tk.Canvas(window, width=1000, height=1000,
                       highlightthickness=0, bg='#AFEEEE')
    canvas.pack()
    fgcolor=color.color()
    Pen(3).bind(canvas)
    menu = tk.Menu(window, tearoff=0)  # 不加 tearoff=0 的会出现可弹出选项
    menu.add_command(label="撤销", command=lambda: Pen(3).re(rev=1))
    menu.add_command(label="恢复", command=lambda: Pen(3).re(rec=1))
    menu.add_command(label="清空", command=Pen(3).clr)
    canvas.bind(
        "<Button-3>", lambda event: menu.post(event.x_root, event.y_root))
    window.mainloop()
