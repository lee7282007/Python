#get_info_list --- push_it

from datetime import datetime
import requests

def get_info_list():
    api = 'https://api.github.com/search/repositories?q='
    query = 'topic:crawler+language:python+'
    when = 'created:' + str(datetime.now()).split()[0]
    full_url = api + query + when
    r = requests.get(full_url)
    return r.json()['item']

def make_message(repo_info):
    title = repo_info['name']
    url = repo_info['html_url']
    message = repo_info['description']
    token = 'xxx'  #这里需要换成你的 token
    user = 'xxx'  #这里需要换成你的 pushover user id
    api = 'https://api.pushover.net/1/messages.json?'
    template = 'token={token}&user={user}&message={msg}&title={t}&url={url}'
    query = template.format(
        token = token,
        user = user,
        msg = message,
        t = title,
        url = url
    )
    full_url = api + query
    return full_url

def push_it(message):
    requests.post(message)
    print('Done')

info_list = get_info_list()
for info in info_list:
    message = make_message(info)
    push_it(message)