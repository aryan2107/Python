import os,re, bs4
import requests
from selenium import webdriver
import ntpath as path
import lxml

url='https://automatetheboringstuff.com/chapter11/'
path=r'C:\Users\aryan\PycharmProjects\classes'
os.chdir(path)
file='comments'
f=open(file,'wb')
res=requests.get(url)
try:
    print ('ERROR CODE OF THE OPENED FILE :-', res.status_code)
    for line in res.iter_content(100000):
        f.write(line)
except Exception as err:
    print ('NOT ABLE TO ACCESS THE URL', err)

f.close()
if os.path.getsize(file) > 1:
    print ('SIZE OF FILE :-',os.path.getsize(file))
    f=open(file)
    bs = bs4.BeautifulSoup(f.read(), 'lxml')
    comments = bs.select('.calibre4')
    print(len(comments), comments)
    if len(comments) > 1:
        for i in range(len(comments)):
            #print(i, '******TH ELEMENT IS:-', comments[i].getText())
            expr='(logs into your email account)'
            match=re.search(expr,comments[i].getText())
            if match:
                print ('MATCHED :-',match.group(1))
                print (comments[i].getText())
                break


else:
    print ('SCRIPT FAILED TO READ THE URL')

