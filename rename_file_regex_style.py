import os
import re
import ntpath as path
import shutil
import time
from datetime import datetime

path=r'C:\\Users\\aryan\\temp_dir_file_python_practice'

os.chdir(path)

now=datetime.now()
mm=now.month
dd=now.day
yyyy=now.year
filename=''

print('month is {0}, date is {1}, year is {2}'.format(mm,dd,yyyy))

if os.path.isdir(path):
    for i in range(1,10):
        print('CREATE RANDOME FILES ON WHICH REGEX SHOULD FAIL')

        filename=str(dd)+'-'+str(mm)+'-'+str(yyyy)+'-RFILE'+str(i)+'.txt'
        f=open(filename,'w')
        f.write('TEMP FILE FOR PRACTICE')

        if os.path.isfile(filename):
           print(filename, ' exists ', ' with size of file ', os.path.getsize(filename))
        else:
            print ('FAILED FOR',filename)
    print('CREATE FILES ON WHICH REGEX SHOULD PASS')

    for i in range(1,10):
        filename=str(mm)+'-'+str(dd)+'-'+str(yyyy)+'file'+str(i)+'.txt'
        f=open(filename,'w')
        f.write('TEMP FILE FOR PRACTICE')

        if os.path.isfile(filename):
           print(filename, ' exists ', ' with size of file ', os.path.getsize(filename))
        else:
            print ('FAILED FOR',filename)

print ('FILES CREATED SLEEPING FOR 30 SEC')
#time.sleep(30)

#expr=r'(?P<DATE>[\d]{0,1})-(?P<MONTH>[\d]{2})-(?P<YEAR>[\d]{4})(?P<FILE>[a-zA-Z0-9]+).(?P<EXT>.*)'
expr=r'(?P<MONTH>((0|1)?\d))-(?P<DATE>((0|1|2|3)?\d))-(?P<YEAR>((19|20)?\d\d))(?P<FILE>[a-zA-Z0-9]+).(?P<EXT>.*)'



for file in os.listdir(path):
    match=re.match(expr,file)
    if match:
       print ('FILE MATCHED:-', file)
       print('day :-{0}, month:- {1}, year:- {2}, filename:- {3}, extension :- {4}'.format(match.group('DATE'),\
            match.group('MONTH'), match.group('YEAR'), match.group('FILE'), match.group('EXT')))
       sub_match=match.group('MONTH')+'-'+match.group('DATE')+'-'+match.group('YEAR')+'-'\
                 +match.group('FILE')+'moved'+'.'+match.group('EXT')
       file_rename=shutil.move(file,sub_match)
       time.sleep(3)
       if file_rename:
          if os.path.isfile(sub_match):
             print(file, ' MOVED TO ', sub_match, 'size of file is ', os.path.getsize(sub_match))


    else:
       print('FILE NOT MATCHED:-', file)



