import requests
import os
import ntpath as path

os.chdir('C:\\Users\\aryan\\PycharmProjects\\classes')



x=requests.get('https://automatetheboringstuff.com/files/rj.txt')
f=open('del_later.txt','w')
try:
    print (x.raise_for_status())
    print (type(x), len(x.text))
    for line in x.text:
          f.write(line)
    f.close()
    f=open('del_later.txt','r')
    x=f.read()
    print ('AFTER FILE READ',len(x))
    print (x[:100])
    
except Exception as err:
    print ('ERROR OCCURED',err)

f.close()
