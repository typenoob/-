# 随想画板

## 项目简介

想象力和创意思维往往需要通过文字或图的方式进行表达，为激发孩子的想象力、培养创造力和执行力，用python程序开发一个有利于孩子创意创作的随想绘图板。

## 快速开始

### 下载我们发布的版本

1. 在右侧的release中选择稳定的版本，选择下载dist.zip文件
2. 解压缩，运行gui.exe程序

### 自行编译

1. 确保机器上安装有python3以上的python和pip
2. 安装依赖模块`pip install -r requirements.tx`
3. 运行gui.py`python ./build/gui.py`

## 目录结构

```
├─build # 生成的gui.py文件
│  ├─assets
│  ├─gui
│  ├─tmp
│  └─__pycache__
├─dist # 生成的exe文件
│  ├─assets
│  └─tmp
├─doodle-classification-server # 基于docker构建涂鸦预测并提供http api的项目
│  ├─docs
│  │  └─assets
│  ├─doodle_classification
│  │  ├─magic_pencil_data
│  │  ├─model
│  │  └─routers
│  ├─notebooks
│  │  └─.ipynb_checkpoints
│  ├─templates
│  └─tests
│      └─data
├─src # 核心源代码

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

### Shape.py

| 名称        | 参数           | 返回                 | 解释                                                         |
| ----------- | -------------- | -------------------- | ------------------------------------------------------------ |
| init        | 笔的厚度(int)  | 无                   | 传入参数笔粗细                                               |
| stopDraw    | 事件           | 无                   | 停止绘画                                                     |
| startDraw   | 事件           | 无                   | 开始绘画                                                     |
| myLine      | 事件           | 无                   | 直线                                                         |
| myLineArrow | 事件           | 无                   | 带箭头的直线                                                 |
| myRect      | 事件           | 无                   | 矩形                                                         |
| myOval      | 事件           | 无                   | 圆形                                                         |
| bind        | canvas，choice | 返回不同选择下的图形 | choice=1选择直线，等于2选择带箭头直线，等于3选择矩形，4为圆形 |

color.py

| 名称    | 参数              | 返回          | 解释                       |
| ------- | ----------------- | ------------- | -------------------------- |
| color() | 笔的颜色局部变量f | 返回笔的颜色f | 弹出选择框进行选择画笔颜色 |

eraser.py

| 名称      | 参数                 | 返回               | 解释                             |
| --------- | -------------------- | ------------------ | -------------------------------- |
| init      | 橡皮擦的选择t（int） | 无                 | 初始化                           |
| startDraw | event事件            | 无                 | 开始绘制空白区域                 |
| stopDraw  | event事件            | 无                 | 停止绘制                         |
| myEraser  | event事件            | 小型或大型的橡皮擦 | 用小型或大型的橡皮擦绘制空白区域 |
| bind      | canvas               | 绘制               | 鼠标单击绘制                     |

drawText（）

| 名称     | 参数      | 返回                       | 解释         |
| -------- | --------- | -------------------------- | ------------ |
| drawText | event事件 | 跳出两个窗口输入文本和字号 | 用来创建文本 |

color2（）

| 名称       | 参数            | 返回                 | 解释           |
| ---------- | --------------- | -------------------- | -------------- |
| color2（） | 图形填充的颜色f | 返回图形要填充的颜色 | 为图形填充颜色 |

thickadd（）

| 名称         | 参数  | 返回             | 解释                 |
| ------------ | ----- | ---------------- | -------------------- |
| thickadd（） | 粗细t | 返回增加后的粗细 | 增加画笔图形边框粗细 |

thickreduce（）

| 名称            | 参数  | 返回             | 解释                   |
| --------------- | ----- | ---------------- | ---------------------- |
| thickreduce（） | 粗细t | 返回变细后的粗细 | 降低画笔图形边框的粗细 |



## 致谢



- [基于浏览器的协作式UI设计工具figma](https://www.figma.com/)
- [ParthJadhav](https://github.com/ParthJadhav)提供的[Tkinter界面快速构建工具](https://github.com/ParthJadhav/Tkinter-Designer)
- [Eonyang](https://github.com/EonYang)提供的[涂鸦分类服务器构建工具](https://github.com/EonYang/doodle-classification-server)
