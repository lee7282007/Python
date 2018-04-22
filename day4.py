import requests
import webbrowser
import time

api = 'https://api.github.com/repos/channelcat/sanic'
web_page = 'https://github.com/channelcat/sanic'
last_update = '2018-02-22T13:46:57Z'
all_info = requests.get(api).json()
curt_update = all_info['updated_at']
print(curt_update)

while True:
    if not last_update:
        last_update = curt_update
    if last_update < curt_update:
        webbrowser.open(web_page)
    time.sleep(600)