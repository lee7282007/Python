# from runpy import run_path
# from tkinter import *
# import multiprocessing
# import os

# # app exe ---> id ---> pid
# # |script| ---> func1 ---> func2 ---> func3 ...
# # |App| ---> display() & {if do()} ---> update() & {if do()


# def make_app():
#     app = Tk()
#     Listbox(name='listb').pack()
#     Button(text='run', command=run_script).pack()
#     Button(text='stop', command=stop_script).pack()

#     return app


# def ui_make_list():
#     listb = app.children['listb']
#     for d in os.listdir():
#         listb.insert(END, d)


# def run_script():
#     listb = app.children['listb']
#     s_path = listb.get(ACTIVE)
#     p = multiprocessing.Process(name='print', target=lambda: run_path(s_path))
#     p.start()


# def stop_script():
#     for p in multiprocessing.active_children():
#         if p.name == 'print':
#             p.terminate()


# def watcher():
#     print(multiprocessing.active_children())
#     listb = app.children['listb']
#     s_path = listb.get(ACTIVE)
#     print(s_path)
#     app.after(1000, watcher)

# if __name__ == '__main__':
#     app = make_app()
#     app.after(100, ui_make_list)
#     app.after(0, watcher)
#     app.mainloop()

from runpy import run_path
from tkinter import *
#from multiprocessing import Process
import multiprocessing
import os
# app exe  --> id --> pid
# |script| --> func1 --> fun2 --> func3 ...
# \App\ --> display() & {if do()} --> update() & {if do()}

def make_app():
    app = Tk()
    Listbox(name='listb').pack()
    Button(text='run',command=run_script).pack()
    Button(text='stop',command=stop_script).pack()
    return app

def ui_make_list():
    listb = app.children['listb']
    for d in os.listdir():
        listb.insert(END,d)

def run_script():
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    p = multiprocessing.Process(name='print',target=lambda :run_path(s_path))
    # 注意：linux/mac系统下可以使用视频中的lambda表达式，windows系统的用户，需要按此方法调用Process模块。
    # p = multiprocessing.Process(name='print', target=run_path, args=(s_path,))
    # 其中，args是target函数中的参数。在windows中，由于不同的系统机制，target不建议使用lambda表达式，很容易产生错误。
    p.start()

def stop_script():
    for p in multiprocessing.active_children():
        if p.name == 'print':
            p.terminate()

def watcher():
    print(multiprocessing.active_children())
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000,watcher)

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(100,ui_make_list)
    app.after(0,watcher)
    app.mainloop()
