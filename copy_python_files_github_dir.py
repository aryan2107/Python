import re
import os
import ntpath as path
import shutil

path = r'C:\Users\aryan\PycharmProjects\classes'

gitpath = r'C:\Users\aryan\git\Python'

os.chdir(path)
expr = r'\.(py)$'
cnt = 0

for file in os.listdir(path):
    if os.path.isfile(file):
        match = re.search(expr, file)
        if match:
            if os.path.isfile(gitpath):
                print(file, 'FILE ALREADY PRESENT')
            else:
                copy = shutil.copy(file, gitpath)
                if copy:
                    print('copy successful for', file)
                    cnt+=1
                else:
                    print('copy failed for', file)


print('COPIED ', cnt, ' FILES')