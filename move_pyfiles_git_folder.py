import re
import os
import ntpath as path
import shutil
# SECOND COMMIT FOR GIT
path=r'C:\Users\Public\Downloads\coding\Python\hackerrank'

newpath=r'C:\Users\aryan\git\Python'


os.chdir(path)
expr=r'\.(py)$'

for file in os.listdir(path):

    if os.path.isfile(file):
       match=re.search(expr,file)
       if match:
          abspath=os.path.abspath(file)
          print('REGEXP MATCHED :-',abspath)

          move=shutil.copy(abspath,newpath)
          if move:
             print('MOVE SUCCESSFUL :-',file)
          else:
             print('MOVE FAILED:-',file)
             break
    else:
        print('DESTINATION DIR ',newpath, ' DOESNT EXIST', file,':', os.getcwd())

