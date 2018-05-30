from pynput.keyboard import Listener, Controller ,Key
import time
import threading


# single_key ->? combo_key

# combo_key? from single key

# presskey -> [] read list -- combokey -- write

# OOP

# get_combo -> parse_combo -> write content

# listener(get_combo) _ combo_reader(parse_combo) _ writer(write content)


class ComboListener:

    def __init__(self):
        self.cur_keys = []
        self.keymap = {
            'bbb': 'wait a minute',
            'aaa': 'good game'
        }
        self._run()
# aaa bbb
    def _on_press(self, key):
        try:
            self.cur_keys.append(key.char)

        except AttributeError:
            self.cur_keys.append(key.name)

    def _cleaner(self):
        while True:
            time.sleep(0.7)
            self.cur_keys.clear()

    def _run(self):
        l = Listener(on_press=self._on_press)
        l.daemon = True
        l.start()

        t = threading.Thread(target=self._cleaner)
        t.daemon = True
        t.start()

    def get_combo(self):
        if len(self.cur_keys) >= 3:
            combo = self.cur_keys[-3:]
            # [a,a,a,a]
            return combo

    def get_parsed_combo(self):
        combo = self.get_combo()
        # [a,a,a]
        if combo:
            key = ''.join(combo)
            # aaa
            if key in self.keymap.keys():
                #[bbb,aaa]
                return self.keymap[key]


def send(content):
    for _ in range(3):
        k.press(Key.backspace)
    k.type(content)




cl = ComboListener()
k  = Controller()

while True:
    combo_content = cl.get_parsed_combo()
    if combo_content:
        send(combo_content)