# 利用askdirectory函数来完成选择输出路径的功能。在显示输出路径的时候，利用StringVar对象来动态的加载其内容。

from tkinter import *
from tkinter.filedialog import *
# from PIL import Image as Img

size_list = [50, 100, 120, 180, 512]

info = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app, text='Image generate tool').pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='open',command = open).pack()
    Button(app, text='generate',command = generate).pack()
    Entry(app, textvariable=out_path)
    Button(app, text='output_path', command=output_path).pack()
    app.geometry('300x400')
    return app

def open():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])

def generate():
    for f_path in info['path']:
        output = out_path.get()
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        # image = Img.resize(image)
        # image.save(output + 'c_' + name,quality=60)
        for s in size_list:
            image.resize((s,s)).save(output+str(s)+"_"+name)

def output_path():
    path = askdirectory()
    out_path.set(path)


app = Tk()
out_path = StringVar()
make_app()
app.mainloop()

# teacher answer, much better than mine

# coding:utf-8
from tkinter import *
from tkinter.filedialog import *
# from PIL import Image as Img

# 将指定的像素大小存到list变量中
size_list = [50, 100, 120, 180, 512]
info = {
    'path':[]
}

# 创建一个GUI框体，这次框里利用grid来管理，以表格的形式组织各控件，使其整齐有序
def make_app():
    Label(app, text='Image compress tool', font=('Hack',20,'bold')).grid(row=0,columnspan=3)
    Listbox(app, name='lbox', bg='#f2f2f2').grid(row=1,columnspan=3)
    Label(app, text='Click to open files:').grid(row=2, column=0)
    Button(app, text='open', command=ui_getdata).grid(row=2,column=1,columnspan=2)
    Label(app, text='Click to resize pictures:').grid(row=3,column=0)
    Button(app, text='resize', command=resize_pic).grid(row=3,column=1,columnspan=2)
    Label(app, text='Set output path:').grid(row=4, column=0)
    Entry(app, textvariable=out_path).grid(row=4,column=1)
    Button(app, text='Select', command=select_path).grid(row=4,column=2)
    app.geometry('400x350')

# 获取文件，并将其展示在listbox组件中
def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])
# 利用resize函数，修改图像大小
def resize_pic():
    for f_path in info['path']:
        output = out_path.get()
        print(output)
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        for s in size_list:
            image.resize((s,s)).save(str(output)+'/'+str(s)+'_'+name)
        print('Finish!')
# 利用askdirectory函数，选择输出文件路径
def select_path():
    path = askdirectory()
    out_path.set(path)

# 实例化Tkinter对象
app = Tk()
# 输出路径是实例化的StringVar对象
out_path = StringVar()
# 调用函数生成框体
make_app()
# 运行Tkinter对象
app.mainloop()
