import re
import os
import ntpath as path
import shutil
# COMMENT
path=r'E:\MAC\Dropbox_bkp\Arista'

newpath=r'E:\MAC\MovedPics'


os.chdir(path)
expr=r'\.(jpg|JPG|jpeg|JPEG|png|PNG)$'

for file in os.listdir(path):

    if os.path.isfile(file):
       match=re.search(expr,file)
       if match:
          abspath=os.path.abspath(file)
          print('REGEXP MATCHED :-',abspath)

          move=shutil.move(abspath,newpath)
          if move:
             print('MOVE SUCCESSFUL :-',file)
          else:
             print('MOVE FAILED:-',file)
             break
    else:
        print('DESTINATION DIR ',newpath, ' DOESNT EXIST', file,':', os.getcwd())

