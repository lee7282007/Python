# import shutil
# import threading
# import os
# from day20exercise_config import CONFIGS

# class ArchiveMonitor:

#     def __init__(self, config):
#         self.source_path = config['source_path']
#         self.target_path = config['target_path']

#     # 移动文件
#     def move(self):
#         shutil.unpack_archive(self.source_path, self.target_path)

#     def monitor(self):
#         files = os.listdir(self.source_path)
#         for file in files:
#             if file.endswith('.zip'):
#                 self.move()    

#     # 多线程
#     def run(self):
#         def _run():
#             while True:
#                 self.monitor()
#         t = threading.Thread(target =_run)
#         t.start()

# archives = [ArchiveMonitor(a) for a in CONFIGS]

# teacher's answer
# coding:utf-8
import os
import shutil
import threading
import time

class ArchiveManager:
    def __init__(self, config):
        # 设置桌面的绝对路径
        self.desktop_path = config["desktop_path"]
        # 设置download文件夹的绝对路径
        self.download_path = config["download_path"]
        # 设置每次监测的间隔时间
        self.interval = config["interval"]
        # 设置压缩包文件的后缀名
        self.suffix = config["suffix"]
        # 设置等待解压的时间
        self.waiting_time = config["waiting_time"]

    # 监测桌面
    def desktop_monitor(self):
        while True:
            for f in os.listdir(self.desktop_path):
                if f.endswith(self.suffix):
                    full_path = os.path.join(self.desktop_path, f)
                    # 解压目标路径
                    target_path = os.path.join(self.desktop_path, f.replace(self.suffix, ""))
                    shutil.unpack_archive(full_path, target_path)
                    time.sleep(self.waiting_time)
                    os.remove(full_path)
            time.sleep(self.interval)

    # 监测download文件夹
    def download_monitor(self):
        while True:
            for f in os.listdir(self.download_path):
                if f.endswith(self.suffix):
                    full_path = os.path.join(self.download_path, f)
                    target_path = os.path.join(self.download_path, f.replace(self.suffix, ""))
                    shutil.unpack_archive(full_path, target_path)
                    package_path = os.path.join(self.download_path, "package")
                    if not os.path.isdir(package_path):
                        os.mkdir(package_path)
                    shutil.move(full_path, package_path)

            time.sleep(self.interval)

    def run(self):
        desktop_thread = threading.Thread(target=self.desktop_monitor)
        desktop_thread.daemon = True
        desktop_thread.start()
        download_thread = threading.Thread(target=self.download_monitor)
        download_thread.daemon = True
        download_thread.start()


if __name__ == "__main__":

    CONFIGS = {
        "desktop_path" : "C:\\Users\\Elmsley\\Desktop\\test1",
        "download_path" : "C:\\Users\\Elmsley\\Desktop\\test2",
        "interval" : 60,
        "suffix" : ".zip",
        "waiting_time" : 10
    }

    test = ArchiveManager(CONFIGS)
    test.run()
    """
    如果设置了daemon，那么，在进程结束的时候，会不考虑线程的运行情况，直接杀死进程。
    对于上面的代码来说，运行之后会直接停止掉两个线程，所以，考虑在进程中加入一个死循环，保证进程一直存在。
    """
    while True:
        pass