import os
import shutil

def scan_file():
    files = os.listdir()
    for f in files:
        if f.endswith('.zip'):
            return f

def unzip_it(f):
    folder_name = f.split('.')[0]
    target_path = './' + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(f, target_path)

def delete(f):
    os.remove(f)

while True:
    zip_file = scan_file()
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)