import re
import os
import ntpath as path
import shutil

path=r'E:\MAC'

newpath=r'E:\MAC\MovedPics'


os.chdir(path)
expr=r'\.(jpg|JPG|jpeg|JPEG|png|PNG)$'
cnt=0



for folder,subfolders, filenames in os.walk(path):
    print ('*' * 60)
    print ('IN FOLDER', folder)

    for subf in subfolders:

        expr1 = r'\\(Pics|MovedPics)$'
        out=re.search(expr1,folder)
        if out:
           print ('IN PICS FOLDER',folder)
           break
        else:
           print('*' * 60)
           print('IN SUBF: ', subf, ' of folder ', folder, len(folder))
           for file in filenames:
               match=re.search(expr,file)
               if match:
                  os.chdir(folder)

                  abspath=os.path.abspath(file)
                  print('REGEXP MATCHED :-',abspath, os.getcwd())
                  try:

                     move=shutil.move(abspath,newpath)
                     print('MOVE SUCCESSFUL :-',file, ' OF SUBFOLDER', subf)
                     cnt+=1
                  except:
                     print('MOVE FAILED:-',file, ' OF SUBFOLDER', subf)


print ('MOVED ',cnt,' FILES')