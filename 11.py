# -*- coding: utf-8 -*-
from math import *
from turtle import *
from graphics import *
import math

def main():
    win = GraphWin("粘滞系数", 400, 300)

    Text(Point(80, 120), "位置维度:").draw(win)

    Text(Point(175, 115), "°").draw(win)
    Text(Point(225, 115), "’").draw(win)
    Text(Point(275, 115), "”").draw(win)

    input0 = Entry(Point(150, 120), 4)
    input0.setText(0)
    input0.draw(win)
    input01 = Entry(Point(200, 120), 4)
    input01.setText(0)
    input01.draw(win)
    input02 = Entry(Point(250, 120), 4)
    input02.setText(0)
    input02.draw(win)

    Text(Point(80, 150), "重力加速度:").draw(win)  # l
    Text(Point(300, 150), "m/s^2").draw(win)
    input1 = Entry(Point(200, 150), 15)
    input1.setText(0.0)
    input1.draw(win)

    win.getMouse()

    m1 = eval(input02.getText())/60
    m2 = (eval(input01.getText()) + m1)/60
    ψ = eval(input0.getText()) + m2
    # print(ψ)
    w = 9.780327 * (1 + 0.0053024 * (math.sin(ψ)) ** 2 - 0.0000058 * (math.sin(2 * ψ)) ** 2)
    input1.setText(w)

    win.getMouse()

main()