import os
path = '/Users/cybermaster/Desktop/images'
files = os.listdir(path)

for f in files:
    if 'fish' in f and f.endswith('.png'):
        print('Found it! ' + f)