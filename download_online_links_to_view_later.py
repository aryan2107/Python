import re,requests,os,bs4
import ntpath as path
import lxml
import time

os.chdir(r'C:\Users\aryan\PycharmProjects\classes')
path1=r'C:\Users\aryan\PycharmProjects\classes\comicbooks'
url = 'http://xkcd.com/'


filename='temp.txt'
next=''
cnt=1
print('INITIAL URL {0} : PWD {1} : filename {2}  '.format(url, os.getcwd(), filename,))
    
while not url.endswith('#'):
      newurl = url + str(next)
      filename1=''
      filename1=path1+'\\'+'dwnld_comic'+str(cnt)+'.png'


      f1 = open(filename1, 'wb')
      f = open(filename, 'wb')
      res = requests.get(newurl)
      if res.status_code == 200:
          for line in res.iter_content(100000):
              f.write(line)

      
      f.close()
      print('NEW URL {0} ::  filename1 {1} '.format(url , filename1))

      f=open(filename)
      if os.path.getsize(filename) > 1:
         bs=bs4.BeautifulSoup(f.read(), 'lxml')
         out=bs.select('#comic img')
         next=bs.select('a[rel="prev"]')[0]
         next=next.get('href')

 
        
         

         if len(out) == 1:
             print ('IMG LINK-',str(out[0].get('src')))
             print ('NEXT LINK is:-', next)
             finalout= 'http:'+ str(out[0].get('src'))
             

             print ('finalout',finalout)
             img_res=requests.get(finalout,stream=True)
             if img_res.status_code==200:
                for line in img_res.iter_content(100000):
                     f1.write(line)

                if os.path.isfile(filename1):
                     if os.path.getsize(filename1):
                        print('DATA DOWNLOADED, SIZE OF FILE :-', os.path.getsize(filename1))
             else:
                 print ('COMIC DIDNT DOWNLOAD',img_res.raise_for_status())
      else:
          print('NOT ABLE TO CREATE THE MAIN FILE:-', filename)
          break

      f.close()
      f1.close()
      cnt+=1
      









