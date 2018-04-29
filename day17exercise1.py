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

def ui_watcher():
    def _update_button():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
            btn['state'] = 'disabled'
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

    def _main():
        while True:
            print("I'm watching you.")
            print(threading.enumerate())
            _get_time()
            _update_time()
            _update_button()
            _update_input()
            time.sleep(0.5)

    t = threading.Thread(target=_main, name='watcher')
    t.start()

app = make_app()
app.after(0, ui_watcher())
app.mainloop()