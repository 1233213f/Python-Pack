# -*- coding: utf-8 -*-
from math import *
from turtle import *
from graphics import *
import math

def main():
    win = GraphWin("粘滞系数", 400, 400)

    Text(Point(80, 15), "重力加速度:").draw(win)  # l
    Text(Point(300, 15), "m/s^2").draw(win)
    input0 = Entry(Point(210, 15), 15)
    input0.setText(0.0)
    input0.draw(win)

    Text(Point(80, 40), "小球下落距离:").draw(win)  # l
    Text(Point(300, 40), "cm").draw(win)
    input5 = Entry(Point(210, 40), 15)
    input5.setText(0.0)
    input5.draw(win)

    Text(Point(80, 65), "小球平均质量:").draw(win)  # m
    Text(Point(300, 65), "g").draw(win)
    input6 = Entry(Point(210, 65), 15)
    input6.setText(0.0)
    input6.draw(win)

    Text(Point(80, 90), "小球平均直径:").draw(win)  # d
    Text(Point(300, 90), "mm").draw(win)
    input7 = Entry(Point(210, 90), 15)
    input7.setText(0.0)
    input7.draw(win)

    Text(Point(80, 115), "量筒内径:").draw(win)  # D
    Text(Point(300, 115), "cm").draw(win)
    input1 = Entry(Point(210, 115), 15)
    input1.setText(0.0)
    input1.draw(win)

    Text(Point(80, 140), "液柱高度:").draw(win)  # H
    Text(Point(300, 140), "cm").draw(win)
    input2 = Entry(Point(210, 140), 15)
    input2.setText(0.0)
    input2.draw(win)


    Text(Point(80, 165), "液体密度:").draw(win)  # p2
    Text(Point(310, 165), "g/cm^3").draw(win)
    input3 = Entry(Point(210, 165), 15)
    input3.setText(0.0)
    input3.draw(win)

    Text(Point(80, 190), "下落时间:").draw(win)  # p1
    Text(Point(310, 190), "s").draw(win)
    input40 = Entry(Point(210, 190), 15)
    input40.setText(0.0)
    input40.draw(win)

    Text(Point(80, 215), "小球密度:").draw(win)  # p1
    Text(Point(310, 215), "g/cm^3").draw(win)
    input4 = Entry(Point(210, 215), 15)
    input4.setText(0.0)
    input4.draw(win)

    Text(Point(80, 240), "粘滞系数:").draw(win)  # d
    Text(Point(310, 240), "g/(cm*s)").draw(win)
    input8 = Entry(Point(210, 240), 15)
    input8.setText(0.0)
    input8.draw(win)

    Text(Point(80, 265), "修正系数:").draw(win)  # d
    Text(Point(300, 265), "").draw(win)
    input9 = Entry(Point(210, 265), 15)
    input9.setText(0.0)
    input9.draw(win)

    Text(Point(80, 290), "粘滞系数:").draw(win)  # d
    Text(Point(310, 290), "g/(cm*s)").draw(win)
    input10= Entry(Point(210, 290), 15)
    input10.setText(0.0)
    input10.draw(win)

    Text(Point(80, 315), "粘滞系数:").draw(win)  # d
    Text(Point(310, 315), "Pa*s").draw(win)
    input11 = Entry(Point(210, 315), 15)
    input11.setText(0.0)
    input11.draw(win)

    Text(Point(210, 350), "点击计算").draw(win)  # p
    # input40 = Entry(Point(210, 350), 15)
    # input40.setText('点击计算')
    # input40.draw(win)

    win.getMouse()
    D = eval(input1.getText())
    H = eval(input2.getText())
    p2 = eval(input3.getText())
    g = eval(input0.getText()) * 100
    l = eval(input5.getText())
    m = eval(input6.getText())
    d = eval(input7.getText()) * 0.1
    t = eval(input40.getText())

    if (math.pi * d ** 3) == 0:
        input4.setText(0.0)
    else:
        p1 = 6 * m / (math.pi * d ** 3)
        input4.setText(p1)

    win.getMouse()
    f1 = (p1 - p2) * g * (d ** 2) * t * 1
    f11 = d / D
    f12 = d / H
    f2 = 18 * l * (1 + 2.4 * f11) * (1 + 1.6 * f12)
    Pas = f1 / f2
    input8.setText(Pas)

    Re = p2 * d * l / (Pas * t)
    input9.setText(Re)

    if Re > 0.1 and Re < 1 :
        Pas1 = Pas/(1+3*Re/16)
    else:
        Pas1 = Pas

    input10.setText(Pas1)
    input11.setText(Pas1/10)
    # Text(Point(80, 150), "和:").draw(win)
    # input3 = Entry(Point(200, 150), 5)
    # input3.draw(win)
    # 点击屏幕求和，求和运算必须是点击鼠标之后，否则参加计算的是默认值
    # win.getMouse()
    # sum = eval(input5.getText()) + eval(input6.getText())
    # # print(eval(input1.getText()))
    # input7.setText(sum)
    win.getMouse()
    # win.close()

main()