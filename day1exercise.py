import os
path = 'E:\JiuzhangAlgrithom20171104\Python实战主义\动手\课时2：如何模糊搜索文件\第一天练习：如何模糊搜索文件'
files = os.listdir(path)

for f in files:
    if  (not f.endswith('.gif')) and ('project30' in f or 'commercial' in f):
        print('Found it! ' + f)