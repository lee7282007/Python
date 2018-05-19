# # UI ---> UI & User ---> UI & User & Core ---> B.E.C

# from tkinter import *
# import time
# import threading
# import multiprocessing
# from runpy import run_path

# data = []

# def make_app():
#     app = Tk()
#     app.geometry('300x400')
#     Button(name = 'add', text = 'add', command = make_task).pack(side = BOTTOM)
#     return app

# def make_task():
#     _font = ['Hack',18,'bold']
#     f = Frame(bg = '#f2f2f2')
#     Label(f, name = 'lb_name', text = 'Script name', bg = '#f2f2f2', font = _font).pack(anchor = 'nw')
#     Label(f, name = 'lb_time', text = 'time', bg = '#f2f2f2').pack(side = LEFT)
#     Button(f, text = ':', command = lambda:make_win(f)).pack(anchor = 'se')
#     f.pack(fill = X)

# def make_win(f):
#     t = Toplevel(f)
#     Label(t,text = 'FILE PATH').pack()
#     Entry(t, name = 'file_ipt').pack()
#     Label(t, text = 'START TIME').pack()
#     Entry(t, name = 'time_ipt').pack()
#     Button(t, text = 'save', command = lambda:(save(t), t.destroy())).pack()

# def save(t):
#     d = {}
#     file_path = t.children['file_ipt'].get()
#     start_time = t.children['time_ipt'].get()
#     d['file_path'] = file_path
#     d['start_time'] = start_time
#     d['execute'] = False
#     data.append(d)
#     # [{}, {}]

# def watcher():
#     def _test():
#         print(data)

#     def _refresh_task():
#         # task ---> data ---> (t --> t_data)
#         # [1,2] [a,b] ---> 1a 2b ---> zip
#         tasks = [t[1] for t in app.children.items() if t[0] != 'add']
#         for d, t in zip(data, tasks):
#             t.children['lb_name']['text'] = d['file_path']
#             t.children['lb_time']['text'] = d['start_time']

#     def _task_check():
#         now = time.ctime().split()[-2]
#         for d in data:
#             if d['start_time'] <= now and not d['execute']:
#                 p = multiprocessing.Process(target = lambda:run_path(d['file_path']))
#                 p = multiprocessing.Process(target=lambda:run_path(d['file_path']))
#                 p.start()
#                 d['execute'] = True

#     def _main():
#         while True:
#             time.sleep(0.5)
#             _test()
#             _refresh_task()
#             _task_check()

#     t = threading.Thread(target = _main, name = 'watcher')
#     t.start()


# app = make_app()
# app.after(0,watcher)
# app.mainloop()


# UI --> UI&User --> UI&User&Core --> B.E.C
# watcher
#
#t -> t_data
#data = [
#    {file_path:123,sart_time:20:00},
#    {file_path:123,sart_time:20:00},
#    {}
#]
from tkinter import *
import threading
import multiprocessing
from runpy import run_path
import time
data = []

def make_app():
    app = Tk()
    app.geometry('300x400')
    Button(name='add',text='add',command=make_task).pack(side=BOTTOM)
    return app

def make_task():
    _font = ['Hack',18,'bold']
    f = Frame(bg='#f2f2f2')
    Label(f,name='lb_name',text='Script name',bg='#f2f2f2',font=_font).pack(anchor='nw')
    Label(f,name='lb_time',text='time',bg='#f2f2f2').pack(side=LEFT)
    Button(f,text=':',command=lambda:make_win(f)).pack(anchor='se')
    f.pack(fill=X)

def make_win(f):
    t = Toplevel(f)
    Label(t,text='FILE PATH').pack()
    Entry(t,name='file_ipt').pack()
    Label(t,text='START TIME').pack()
    Entry(t,name='time_ipt').pack()
    Button(t,text='save',command=lambda:(save(t),t.destroy())).pack()

def save(t):
    d = {}
    file_path  = t.children['file_ipt'].get()
    start_time = t.children['time_ipt'].get()
    d['file_path']  = file_path
    d['start_time'] = start_time
    d['execute'] = False
    data.append(d)
    # [{},{}]

def watcher():
    def _test():
        print(data)

    def _refresh_task():
        # task --> data --> (t -> t_data)
        # [1,2] [a,b] --> 1a 2b ---> zip
        tasks = [t[1] for t in app.children.items() if t[0] != 'add'] #(key,value) children['key'] --> value
        for d,t in zip(data,tasks):
            t.children['lb_name']['text'] = d['file_path']
            t.children['lb_time']['text'] = d['start_time']

    def _task_check():
        now = time.ctime().split()[-2]

        for d in data:
            if d['start_time'] <= now and not d['execute']:
                # p = multiprocessing.Process(target=lambda:run_path(d['file_path']))
                # 注意：linux/mac系统下可以使用视频中的lambda表达式，windows系统的用户，需要按此方法调用Process模块。
                p = multiprocessing.Process(target=run_path, args=(d['file_path'],))
                # 其中，args是target函数中的参数。在windows中，由于不同的系统机制，target不建议使用lambda表达式，很容易产生错误。
                p.start()
                d['execute'] = True


    def _main():
        while True:
            time.sleep(0.5)
            _test()
            _refresh_task()
            _task_check()

    t = threading.Thread(target=_main,name='watcher')
    t.start()

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(0,watcher)
    app.mainloop()