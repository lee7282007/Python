from wxpy import *
import time
#初始化机器人，扫码登录
bot = Bot()

def listen(pwd):
    time.sleep(3)
    return [msg for msg in bot.messages if msg.text == pwd]

def add(users, group):
    try:
        group.add_members(users, use_invitation = True)
        return group
    except ResponseError:
        return None

def get_newfren(say):
    time.sleep(3)
    return [msg for msg in bot.messages if msg.text == say]

group = bot.groups().search('test group 1')[0]

while True:
    new_fren = get_newfren('Make friend')
    if new_fren:
        for msg in new_fren:
            new_user = msg.card
            bot.accept_friend(new_user)
            new_user.send('Hi new friend')
            bot.messages.remove(msg)

    time.sleep(3)

    print('Running')
    selected = listen('Pull me in')
    if selected:
        print('Found a new friend! XD')
        for msg in selected:
            this_user = msg.sender
            add(this_user, group)
            bot.messages.remove(msg)

