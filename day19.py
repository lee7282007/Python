# build space -> choose space -> switch space
# How we start OOP ? -> space

'''
folder

choose = input()
if choose == workspace.name:
    workspace.switch()

'''
from subprocess import call
import os
from day19sconfig import CONFIGS

class WorkSpace:

    def __init__(self, c):
        self.folders = c['folders']
        self.name    = c['name']
        self.target  = c['target']

    def switch(self):
        for f in os.listdir(self.target):
            # xxx.wspc
            if f.endswith('.wspc'):
                path = self.target + f
                os.remove(path)
        # mklink
        # 以下部分是视频中 OS 系统的写法，其他代码一致
        for source in self.folders:
            real_target = self.target + source.split('/')[-1] + '.wspc'
            command = ['ln','-s', source, real_target]
            # python -m xxx.py
            call(command)

        # 以下部分是 Windows 系统的写法，其他代码一致。另外由于 windows 系统运行 MKLINK 需要管理员权限，推荐使用 cmder 运行 http://www.jeffjade.com/2016/01/13/2016-01-13-windows-software-cmder/，或者用管理员身份打开cmd，然后运行python script_lesson_7.py.
        for source in self.folders:
            real_target = self.target + source.split('\\')[-1] + '.wspc'
            command = ['MKLINK','/D', real_target, source]
            # WINDOWS下使用os.system
            os.system(' '.join(command))

workspaces = [WorkSpace(c) for c in CONFIGS]
print('Choose your workspace:')
choice = input()
for w in workspaces:
    if w.name == choice:
        w.switch()