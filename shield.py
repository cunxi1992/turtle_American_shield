# -*- coding:utf-8 -*-
import turtle
import math

def shield():
    '''
    该函数的作用是画一个美国队长的盾牌
    '''
    # 设置画布背景
    turtle.bgcolor('#FFFFFF')
    # 设置画笔速度
    turtle.speed(10)
    # 依次填充同心圆
    fill_circle('#FF0000', 230)
    fill_circle('#FFFFFF', 178)
    fill_circle('#FF0000', 129)
    fill_circle('#0000FF', 75)
    # 完成五角星
    draw_five('#FFFFFF', 75)
    # 以下代码，将画好的图案按指定格式保存到当前文件目录
    # windows 可以使用.jpg格式，MAC使用eps格式
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="shield.eps")

    # 启动事件循环，必须是乌龟图形程序中的最后一个语句
    # 如果没有这个语句，代码运行完成后，窗口直接消失。
    turtle.done()


def draw_circle(radium):
    '''
    该函数的作用是画一个圆线
    :param radium：半径
    '''
    # 画笔定位到圆点
    turtle.home()
    # 提笔
    turtle.penup()
    # 向前移动指定的半径
    turtle.forward(radium)
    # 落笔
    turtle.pendown()
    # 偏转角度
    turtle.setheading(90)
    # 画一个指定半径的圆
    turtle.circle(radium)
    # 提笔
    turtle.penup()


def fill_circle(color, r1):
    '''
    该函数的作用是，画一个圆环，有指定的填充色和半径
    :param color:颜色
    :param r1:半径
    '''
    # 设置画笔颜色
    turtle.pencolor(color)
    # 设置填充颜色
    turtle.fillcolor(color)
    # 开始填充
    turtle.begin_fill()
    # 画圆线
    draw_circle(r1)
    # 结束填充
    turtle.end_fill()

# 画并填充五角星
def draw_five(color, radium):
    '''
    该函数的作用是画一个五角星
    :param color:颜色
    :para radium:
    '''
    # 画笔定位到圆点
    turtle.home()
    # 提笔
    turtle.penup()
    # 偏转90度
    turtle.setheading(90)
    # 向前移动90个像素
    turtle.forward(radium)
    # 偏转288度
    turtle.setheading(288)
    # 落笔
    turtle.pendown()
    # radians()将角度转换为弧度
    long_side = (math.sin(math.radians(36))*radium)/math.sin(math.radians(126))
    # 设置画笔颜色
    turtle.pencolor(color)
    # 设置填充颜色
    turtle.fillcolor(color)
    # 开始填充
    turtle.begin_fill()
    for i in range(10):
        turtle.forward(long_side)
        if i % 2 == 0:
            turtle.left(72)
        else:
            turtle.right(144)
    # 结束填充
    turtle.end_fill()
    # 提笔
    turtle.penup()

# 运行主函数
shield()


