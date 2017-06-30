import os
import re
import ntpath as path
import shutil
import time
from datetime import datetime

path=r'E:\MAC\MovedPics'
#newpath=r'E:\MAC\Pics\New_Pics'




'''
#expr=r'^[0-9][0-9a-z]+.(jpeg)$'
#expr1=r'^[\d]{1,2}_[\d]{1,2}.(jpg)$'
expr=r'^(Note_).*$'
for file in os.listdir(newpath):
    #print(file,len(file))
    #time.sleep(2)
    match=re.match(expr,file)
    if match:
       print('match successful for file', file)
       move=shutil.move(file,newpath)
       if move:
          print(move, ' MOVE SUCCESSFUL FOR FILE ', file)

'''
f=open('E:\\fileExt3.txt','w')

for file in os.listdir(path):
    os.chdir(path)
    dupname=1
    #print (file, os.path.getctime(file))
    if str(file).startswith('201'):
       print('SKIPPING ',file)
    else:

       if os.path.isfile(file):
          timeCreated=os.stat(file)
          timeCreated=timeCreated.st_mtime
          timeCreated=datetime.utcfromtimestamp(timeCreated)
          #print (file,' WAS CREATED ON:- ', timeCreated)
          str_timeC=str(timeCreated)
          expr=r'\.(?P<ext>[a-zA-Z]{2,4})$'
          out=re.search(expr,file)
          if out:
             match = re.sub('[:.\s]', '-', str_timeC)

             if str(file).endswith(out.group('ext')):
                match=match+'.'+out.group('ext')


                move=shutil.copy(file,match)
                #time.sleep(2)
                if move:
                   print(match, file=f)

                else:
                   print('MOVED FAILED FOR :-',file)
                   break
             else:
                print('ENDSWITH FAILED FOR:-',file)
          else:
             print('REGEX FAILED',file)
             break



'''

for file in os.listdir(path):
    file1=str(file)+'.jpg'
    print(file1)
    move = shutil.move(file, file1)
    if move:
        pass
    else:
        print('MOVE UNSUCCESSFUL FOR:- ', file)

'''