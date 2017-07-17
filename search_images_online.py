import requests,bs4
import os
import ntpath as path
import webbrowser
import sys
import re
import lxml

url='https://images.google.com/?gws_rd=ssl'
keyword=''
filename='image_search_results.txt'

print (sys.argv, type(sys.argv))
if len(sys.argv )> 1:
    for i in sys.argv[1:]:
        keyword=keyword+' '+i
print('KEYWORD IS:-',keyword)

expr=r'^(\s+)(.*)'

keyword=re.search(expr,keyword)
if keyword:
    print ('regexp matched:-', keyword.group(2))
    url = url + keyword.group(2)
    print('KEYWORD IS:-',keyword.group(2), 'URL IS', url)

os.chdir('C:/Users/aryan/PycharmProjects/classes')
f=open(filename,'wb')
res=requests.get(url,stream=True)
if res.status_code==200:
    for line in res.iter_content(100000):
        f.write(line)
    f.close()
else:
    print ('WEBPAGE DIDNT LOAD:-', res.raise_for_status())

if os.path.isfile(filename):
   print ('file created:-', os.path.getsize(filename))
   f=open(filename,'r')
   fileread=f.read()
   bs=bs4.BeautifulSoup(fileread,'lxml')
   output=bs.select('.rg_ic .rg_i')
   if len(output) > 1:
       for i in range(len(output)):
           link=''
           link=output[i].get('src')
           print (i,'TH LINK FOR UR SEARCH IS:-',link)
           #b=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
           #print ('b :-',b)
           #browser = webbrowser.get(b)
           if i==0:
              print ('opening new WINDOW:-','http://google.com'+link)
              #browser.open_new('http://google.com'+link)
              webbrowser.open('http://google.com'+link, new=1,autoraise=True)
           elif i > 0 and i < 4:
               webbrowser.open_new('http://google.com'+link,)
               print('opening new TAB:-', 'http://google.com' + link)
               #browser.open_new_tab('http://google.com' + link)
           else:
               print('WEBBROWSER NOT OPENING')






