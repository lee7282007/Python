import time
from tkinter import *
import keyboard

def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    Label(
        text='Typing Speed Monitor',
        font=('Hack', 25, 'bold'),
        bg='#303030',
        fg='white').pack()

    Label(
        name='lb2',
        text='_char/s',
        font=('Hack', 20, 'bold'),
        bg='#303030',
        fg='white').pack()
    return app


def speed_test():
    # s1 = psutil.net_io_counters(pernic=True)['无线网络连接']
    keyboard.start_recording()
    time.sleep(1)
    # s2 = psutil.net_io_counters(pernic=True)['无线网络连接']
    s =keyboard.stop_recording()
    # result = s2.bytes_recv - s1.bytes_recv
    speed = len(s) // 2
    return str(speed) + 'char/s'


def ui_update(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    app.after(1000, lambda: ui_update(do))


app = make_app()
app.after(1000, lambda: ui_update(speed_test))
app.mainloop()

# teacher's answer
# coding:utf-8

# from tkinter import *
# import keyboard
# import time
# # 创建GUI框体
# def make_app():
#     app = Tk()
#     app.geometry('300x150')
#     app.config(bg='#303030')
#     Label(text='Typing Speed Monitor',
#           font=('Hack',25,'bold'),
#           bg='#303030',
#           fg='white').pack()

#     Label(name='lb2',
#           text='_char/s',
#           font=('Hack',20,'bold'),
#           bg='#303030',
#           fg='white'
#           ).pack()
#     return app
# # 利用keyboard库，监测键盘敲击速度
# def keyboard_test():
#     keyboard.start_recording()
#     time.sleep(1)
#     s = keyboard.stop_recording()
#     # 获取的列表中，包含了一个按键的“down”事件和“up”事件
#     # 所以列表的长度除以2，即为敲击按键的次数
#     speed = len(s)//2
#     return str(speed) + " char/s"
# # 动态更新敲击速度
# def ui_update(do):
#     data = do()
#     lb2 = app.children['lb2']
#     lb2.config(text=data)
#     app.after(1000, lambda: ui_update(do))

# # 启动框体
# app = make_app()
# app.after(1000, lambda: ui_update(keyboard_test))
# app.mainloop()