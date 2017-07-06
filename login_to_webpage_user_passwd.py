import requests
import os

os.chdir('C:\\Users\\aryan\\PycharmProjects\\classes')
res=requests.get('https://www.freelancer.in', auth=('seemasam2113@gmail.com', 'Ramada702'))
print (res.raise_for_status())
line=''
f=open('del_later.txt','wb')
for line in res.iter_content(100000):
      f.write(line)

f.close()

print ('THE CONTENTS OF THE FILE ARE')
f=open('del_later.txt','r')
x=f.read()

print (x[:1000])
