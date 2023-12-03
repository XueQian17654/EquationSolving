#  Copyright (c) 2019 - 2039 XueQian  #
#         version_added:: 4.0          #
#         -*- coding:utf-8 -*-        #
from fractions import Fraction
from math import *
import time
import tkinter
from tkinter import ttk
import os
import threading
import easygui
import random

"./CMSXTJ.ttf"

fun = {}


def setvaluefun(button, inputer):
    global fun
    button.config(state="disabled")
    code = easygui.textbox(codebox=True)
    if code != '':
        name = f'x{random.randint(10000, 99999)}(x)'
        # print(f'def {name}:\n    ' + code.replace('\n', '\n    '))
        # print(f'global {name[:-3]}')
        exec(f'def {name}:\n    ' + code.replace('\n', '\n    '))
        exec(f'fun["{name[:-3]}"] = eval(name[:-3])')
        inputer.delete(0, tkinter.END)
        inputer.insert(0, f'fun["{name[:-3]}"](x)')
        # print(fun)
    return button.config(state="normal")


def start(function, text, button):
    global fun
    button.config(state="disabled")
    if not function:
        text.configure(text='请输入函数！')
        return button.config(state="normal")
    function = eval(f'(lambda x: {function})')
    num = -100
    jie = []
    while num <= 100:
        jie.append(num)
        jin = 1
        num += jin
        old = function(num)
        while abs(jin) > 0.0000000000000001 and num <= 100:
            guo = ''
            for i in range(len(jie)):
                guo += f'x{i + 1}={jie[i]}; '
            text.configure(text=guo)
            time.sleep(0.001)

            num += jin
            now = function(num)
            # print([now])
            if now != 0 and not now:
                text.configure(text='没有设置返回值！')
                return button.config(state="normal")
            # print(num, now, jin)
            jie[-1] = num
            if now == 0 or abs(now - 0) < 1e-14:
                # print(9998)
                break
            elif old * now < 0:
                jin = - jin / 10
            # elif old == now and abs(now - 0) < 1e-15:
            #     del jie[-1]
            #     break
            old = now
    if not abs(function(jie[-1])) < 1e-15:
        del jie[-1]

    # print(8889, jin)
    guo = ''
    for i in range(len(jie)):
        guo += f'x{i + 1}={jie[i]}; '
    text.configure(text='在 (-100, +100] 中无异号零点或整数零点' if guo == '' else ('姐数超出限制' if len(jie) > 40 else guo))
    return button.config(state="normal")


if __name__ == '__main__':
    font = "simsun"

    r1 = tkinter.Tk()
    r1.geometry("530x180")
    r1.title('函数的姐')
    r1.resizable(width=True, height=False)

    style = ttk.Style(r1)

    # 加载自定义字体文件
    # style.font_create("custom_font", font="./CMSXTJ.ttf")

    # ('CMSXTJ', 15, "bold")
    tkinter.Label(r1, text='线性函数异号零点求解 XueQian', font=(font, 15, "bold"), foreground='#f60',
                  background='#f0f0f0').place(x=10, y=5)

    tkinter.Label(r1, text='函数：', font=(font, 15), foreground='#000',
                  background='#f0f0f0').place(x=10, y=40)

    s1 = tkinter.Entry(r1, font=(font, 15), bd=4, width=30)
    s1.place(x=70, y=40)
    s1.insert(0, 'x')

    setvaluebutton = tkinter.Button(r1, text='设置分段函数', command=lambda: setvaluefun(setvaluebutton, s1),
                                    font=(font, 15),
                                    foreground='#000')
    setvaluebutton.place(x=385, y=36)

    tkinter.Label(r1, text='结果：', font=(font, 15), foreground='#000',
                  background='#f0f0f0').place(x=10, y=90)

    res = tkinter.Label(r1, text='x1=0; ', font=(font, 15), foreground='#000',
                        background='#f0f0f0')
    res.place(x=70, y=90)

    startb = tkinter.Button(r1, text='开始', command=lambda: eval(
        'threading.Thread(target=lambda: start(s1.get(), res, startb)).start()'), font=(font, 15),
                            foreground='#000')
    startb.place(x=10, y=130)

    tkinter.Button(r1, text='屏幕键盘', command=lambda: os.popen('osk'), font=(font, 15), foreground='#000').place(
        x=100, y=130)
    r1.mainloop()
