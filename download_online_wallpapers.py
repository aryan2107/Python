import re,requests,os,bs4
import ntpath as path
import lxml
import time

os.chdir(r'C:\Users\aryan\PycharmProjects\classes')
path1=r'C:\Users\aryan\PycharmProjects\classes\wallpapers'
url = 'https://www.pexels.com/search/HD%20wallpaper/'


filename='wallpapertemp.txt'
print(' URL {0} : PWD {1} : filename {2}  '.format(url, os.getcwd(), filename,))
f = open(filename, 'wb')
res = requests.get(url)
if res.status_code == 200:
    for line in res.iter_content(100000):
        f.write(line)

f.close()

f=open(filename)
bs=bs4.BeautifulSoup(f.read(), 'lxml')
out=bs.select('.photos img')
print ('NO OF IMAGES TO BE DOWNLOADED:-',len(out), ' & out :-',out)
if os.path.getsize(filename) > 1:
    for i in range(len(out)):
        filename1=''
        filename1=path1+'\\'+'wallpaper'+str(i)+'.jpeg'
        f1 = open(filename1, 'wb')
        print('NEW filename1:- {0} '.format(filename1))





        if len(out) > 1:
             finalout=str(out[i].get('src'))
             print ('finalout',finalout)
             img_res=requests.get(finalout,stream=True)
             if img_res.status_code==200:
                for line in img_res.iter_content(100000):
                     f1.write(line)

                if os.path.isfile(filename1):
                     if os.path.getsize(filename1):
                        print('DATA DOWNLOADED, SIZE OF FILE :-', os.path.getsize(filename1))
             else:
                 print ('WALLPAPER DIDNT DOWNLOAD',img_res.raise_for_status())
                 break
        f1.close()
else:
    print('NOT ABLE TO CREATE THE MAIN FILE:-', filename)



      









