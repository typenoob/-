# 随想画板

## 项目简介

想象力和创意思维往往需要通过文字或图的方式进行表达，为激发孩子的想象力、培养创造力和执行力，用python程序开发一个有利于孩子创意创作的随想绘图板。

## 目录结构

```
│  1.py
│  demo.py
│  README.md
│  requirements.txt # 依赖的pip模块
│
├─build # 利用Tkinter-Designer构建的界面
│  │  gui.py
│  │
│  └─assets
├─doodle-classification-server # 基于docker构建涂鸦预测并提供http api的项目
│
├─mmm # 用到的多媒体素材
│      logo.png
│      test.png
│
└─src # 源代码
    │  main.py
    │  pen.py
    │  predict.py
    │  function.py
```

## 提供的类或函数接口

### pen.py

| 名称     | 参数                      | 返回   | 解释                                     |
| -------- | ------------------------- | ------ | ---------------------------------------- |
| Pen      | 笔的厚度(int)             | 笔对象 | 创建画笔对象                             |
| Pen.bind | 画布(tkinter.Canvas)      | 无     | 绑定画笔至输入的画布                     |
| Pen.re   | 撤销rev(int),恢复rec(int) | 无     | rev=1撤销上次的画迹，rec=1恢复上次的撤销 |

### predict.py

| 名称    | 参数                     | 返回                     | 解释                                             |
| ------- | ------------------------ | ------------------------ | ------------------------------------------------ |
| encode  | 文件路径(string)         | 图片的base64编码(string) | 将一个图片文件base64编码                         |
| predict | 图片的base64编码(string) | 预测的json字符串(string) | json的prediction->name提供了前五可能性的物体名称 |

### function.py

| 名称        | 参数 | 返回       | 解释           |
| ----------- | ---- | ---------- | -------------- |
| message     | 无   | 返回提示框 | 提示未选择粗细 |
| stopDraw    | 事件 | 无         | 停止绘画       |
| startDraw   | 事件 | 无         | 开始绘画       |
| mysave      | 事件 | 暂无完成   | 保存           |
| myyqt       | 事件 | 无         | 油漆桶         |
| myLine      | 事件 | 无         | 直线           |
| myLineArrow | 事件 | 无         | 箭头直线       |
| myRect      | 事件 | 无         | 矩形           |
| myOval      | 事件 | 无         | 椭圆           |
| myPen       | 事件 | 无         | 画笔           |
| myErasor    | 事件 | 无         | 橡皮擦         |



## 致谢



- [基于浏览器的协作式UI设计工具figma](https://www.figma.com/)
- [ParthJadhav](https://github.com/ParthJadhav)提供的[Tkinter界面快速构建工具](https://github.com/ParthJadhav/Tkinter-Designer)
- [Eonyang](https://github.com/EonYang)提供的[涂鸦分类服务器构建工具](https://github.com/EonYang/doodle-classification-server)
