import os
import ntpath as path
import zipfile
import time

path=r'C:\\Users\\aryan\\temp_dir_file_python_practice'
os.chdir(path)



filename=''
if os.path.exists(path):
    #path = r'C:\\Users\\aryan\temp_dir_file_python_practice'
    for i in range(1,10):
        filename=path + r'\\file' + str(i) + '.txt'
        print('CREATING FILE', filename)
        f=open(filename,'w')
        f.write('THIS IS A TEMP FILE CREATED FOR PRACTISING FILE OPERATIONS \
in PYTHON PROGRAMMING LANGUAGE')

        if os.path.exists(filename):
           print (filename, ' exists with SIZE OF FILE :-', os.path.getsize(filename))

else:
    print('FILE PATH DOESNT EXISTS')


print('SLEEPING FOR 10 SEC')
time.sleep(2)

newzip=zipfile.ZipFile('zipall.zip','w')

for i in os.listdir(path):
    file=path+r'\\'+i
    print ('THE FILE IS',file)
    newzip.write(file, compress_type=zipfile.ZIP_DEFLATED)
    print('SLEEPING FOR 2 SEC')
    time.sleep(2)
newzip.close()
print ('READING THE CONTENTS OF ZIPFILE')
print('SLEEPING FOR 2 SEC')
time.sleep(2)
nzip=zipfile.ZipFile('zipall.zip','r')
nzip.namelist()
nzip.close()


print ('GOING TO EXTRACT THE CONTENTS OF THE ZIP FILE')

newpath=path+r':\\tempdir'
print ('newpath is ',newpath)
os.chdir(path)
os.mkdir('tempdir')
newzip = zipfile.ZipFile('zipall.zip')
newzip.extractall()
newzip.close()

if os.path.isdir(newpath):
   print('DIR CREATED SUCCESSFULLY')
   newzip=zipfile.ZipFile('C:\\Users\\aryan\\temp_dir_file_python_practice\\zipall.zip')
   newzip.extractall(newpath)
   for i in os.listdir(newpath):
       print('files at the newpath are :-', i)



