# UI ---> UI & User ---> UI & User & Core ---> B.E.C

from tkinter import *
def make_app():
    app = Tk()
    app.geometry('300x400')
    Button(name = 'add', text = 'add', command = make_task).pack(side = BOTTOM)
    return app

def make_task():
    _font = ['Hack',18,'bold']
    f = Frame(bg = '#f2f2f2')
    Label(f, text = 'Script name', bg = '#f2f2f2', font = _font).pack(anchor = 'nw')
    Label(f, text = 'time', bg = '#f2f2f2').pack(side = LEFT)
    Button(f, text = ':', command = lambda:make_win(f)).pack(anchor = 'se')
    f.pack(fill = X)

def make_win(f):
    t = Toplevel(f)
    Label(t,text = 'FILE PATH').pack()
    Entry(t, name = 'file_ipt').pack()
    Label(t, text = 'START TIME').pack()
    Entry(t, name = 'time_ipt').pack()
    Button(t, text = 'save')


app = make_app()
app.mainloop()