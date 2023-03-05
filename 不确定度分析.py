# -*- coding: utf-8 -*-
from math import *
from turtle import *
from graphics import *
import math

def main():
    
    win = GraphWin("粘滞系数不确定度计算", 400, 300)

    D = 6.416
    ρ = 0.9660
    r = 2.980/2
    H = 38.66

    Text(Point(80, 50), "U(t):").draw(win)
    Text(Point(80, 80), "U(D):").draw(win)
    Text(Point(80, 110), "U(ρ):").draw(win)
    Text(Point(80, 140), "U(r):").draw(win)
    Text(Point(80, 170), "U(H):").draw(win)
    Text(Point(80, 200), "U(l):").draw(win)

    input1 = Entry(Point(140, 50), 8)
    input1.setText(0.0)
    input1.draw(win)
    input2 = Entry(Point(140, 80), 8)
    input2.setText(0.0)
    input2.draw(win)
    input3 = Entry(Point(140, 110), 8)
    input3.setText(0.0)
    input3.draw(win)
    input4 = Entry(Point(140, 140), 8)
    input4.setText(0.0)
    input4.draw(win)
    input5 = Entry(Point(140, 170), 8)
    input5.setText(0.0)
    input5.draw(win)
    input6 = Entry(Point(140, 200), 8)
    input6.setText(0.0)
    input6.draw(win)

    input7 = Entry(Point(300, 46), 16)
    input7.setText(0.0)
    input7.draw(win)

    input8 = Entry(Point(300, 96), 16)
    input8.setText(0.0)
    input8.draw(win)

    input9 = Entry(Point(300, 146), 16)
    input9.setText(0.0)
    input9.draw(win)

    Text(Point(300, 20), "计算出来的粘滞系数").draw(win)
    Text(Point(300, 70), "小球下落距离平均值").draw(win)
    Text(Point(300, 120), "小球下落时间平均值").draw(win)
    # Text(Point(300, 120), "结            果").draw(win)
    Text(Point(140, 240), "点击计算").draw(win)
    Text(Point(300, 220), "粘滞系数不确定度").draw(win)

    input10 = Entry(Point(300, 260), 16)
    input10.setText(0.0)
    input10.draw(win)

    win.getMouse()

    m1 = (eval(input1.getText())**2)/eval(input9.getText())**2
    m2 = (eval(input2.getText())**2)/D**2
    m3 = (eval(input3.getText()) ** 2) / ρ**2
    m4 = (eval(input4.getText()) ** 2) / r ** 2
    m5 = (eval(input5.getText()) ** 2) / H ** 2
    m6 = (eval(input6.getText()) ** 2) / eval(input8.getText())**2

    U = eval(input7.getText())*(m1+m2+m3+m4+m5+m6)**0.5

    input10.setText(U)

    win.getMouse()

main()