# -*- coding:utf-8 -*-
import turtle
turtle.speed(30)
for i in range(360):
    # 偏转角度
    turtle.setheading(i)
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
# windows 可以使用.jpg格式，MAC使用eps格式
ts = turtle.getscreen()
ts.getcanvas().postscript(file="shield.eps")
turtle.done()