# core: find_url -> check_time -> sent_to_browser
# code : ReadManger(c) -> (Tool & Context) manager.run()

from day20r_config import CONFIGS
from time import ctime
import os
import threading
import webbrowser

class ReadManager:

    def __init__(self, config):
        self.read_time = config['time']
        self.folder_path = config['folder_path']
        self.urls = self.urls_parse(self.folder_path) # [www,www,]


    def urls_parse(self,path):
        urls = []
        for f in os.listdir(path):
            if not f.startswith('.'):
                full_path = path + f
                with open(full_path,'r') as raw_url:
                    url = raw_url.read().split('URL=')[-1].strip('\n')
                    print(url)
                    urls.append(url)
        return urls

    def time_to_read(self):
        return self.read_time == ctime().split()[-2]

    def send_to_browser(self):
        for url in self.urls:
            webbrowser.open_new_tab(url)

    def run(self):
        # use threading
        def _run():
            while True:
                if self.time_to_read():
                    self.send_to_browser()
        t = threading.Thread(target=_run)
        t.daemon = True
        t.start()


managers = [ReadManager(c) for c in CONFIGS]
# for m in managers:
#     m.run()