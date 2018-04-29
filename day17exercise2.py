import time
from tkinter import *
# from multiprocessing import Process
import threading

info = {
    # at first write 'total_time:60', the below _update_time method report error
    'total_time':60
}
def make_app():
    _font = ['Hack', 25, 'bold']
    app = Tk()
    Label(name='lb',text = 0,font = _font).pack()
    Button(name = 'btn',text = 'start',command = time_counts).pack()
    Entry(name='ipt').pack()
    app.geometry('300x150')
    return app

def time_counts():
    def _counts():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts, name='timer')
    t.start()

def time_stop():
    info['total_time'] = 0

def ui_watcher():
    def _update_button():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
            btn['state'] = 'normal'
        else:
            btn['state'] = 'normal'

    def _get_time():
        ipt = app.children['ipt']
        # timer is a list, its length is 0 or 1, looks like a true/false, so the if condition below can use as 'if not timer'
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())


    def _update_time():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    # new function
    def _update_input():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
    #         forbid input
            ipt['state'] = 'disabled'
        else:
    #         permit input
            ipt['state'] = 'normal'

    # teacher's answer
    # 将input框禁用的函数
    # def _update_input():
    #     ipt = app.children['ipt']
    #     timer = [t for t in threading.enumerate() if t.name == 'timer']
    #     ipt['state'] = 'disabled' if timer else 'normal'


    # new function
    def start_stop():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
            btn['text'] = 'stop'
            btn['command'] = time_stop
        else:
            btn['text'] = 'start'
            btn['command'] = time_counts

    # teacher's answer
    # 修改按钮状态的函数
    # def _update_button():
    #     btn = app.children['btn']
    #     timer = [t for t in threading.enumerate() if t.name == 'timer']
    #     btn['text'] = '停止' if timer else '开始'
    #     btn['command'] = time_stop if timer else time_counts

    def _main():
        while True:
            print("I'm watching you.")
            print(threading.enumerate())
            _get_time()
            _update_time()
            _update_button()
            _update_input()
            start_stop()
            time.sleep(0.5)

    t = threading.Thread(target=_main, name='watcher')
    t.start()

app = make_app()
app.after(0, ui_watcher())
app.mainloop()