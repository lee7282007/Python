from tkinter import *
import os
import pip

app = Tk()
label = Label(text='Hidden Python Repo', font=('Hack',25,'bold'))
label.pack()
repo_list = pip.get_installed_distributions()

listbox = Listbox(bg = '#f2f2f2', fg = 'black')
listbox.pack(fill = BOTH, expand = True)
for l in repo_list:
    listbox.insert(END,l)
app.mainloop()

# teacher answer
# coding:utf-8
# from tkinter import *
# import pip
#
# # 获取python安装的第三方包，存入字典类型变量中
# installed_packages = pip.get_installed_distributions()
# # 创建窗口实例
# app = Tk()
# # 调整窗口标题的字体字号和内容
# label = Label(text='Python Packages',font=('Hack',20,'bold'))
# label.pack()
# # 在窗口加入listbox框体
# listbox = Listbox(bg='#f2f2f2',fg='red')
# listbox.pack(fill=BOTH,expand=True)
# # 将python第三方包的信息插入到listbox中
# for i in installed_packages:
#     listbox.insert(END,i.key)
# # 显示窗口
# app.mainloop()
# #app.run()
