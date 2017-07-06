
import re
import traceback
import os

def func1(name, bike, car):

    expr=r'^[a-zA-Z]+$'
    match1=re.search(expr,name)
    match2 = re.search(expr, bike)
    match3 = re.search(expr, car)
    print ('{0} :{1} : {2}'.format(match1,match2, match3))


    if match1 and match2 and match3:
       if name=='aryan':
          print (name, ' HAD ', bike ,' & CAR IS ', car )
       else:
          print ('NO USER FOUND')
    else:
        raise Exception('PLEASE PASS A STRING AGAINST THE NAME,BIKE,CAR ARGUMENT ')
path=os.getcwd()
logfile=os.path.join(path,'log.txt')
print ('THE PATH IS', path, 'LOGFILE IS',logfile)
f=open(logfile,'w')

try:
    #name = input('PLEASE ENTER THE NAME:-')
    #bike = input('PLEASE ENTER THE BIKE NAME:-')
    #car = input('PLEASE ENTER THE CAR NAME:-')
    func1(1, 'zx', 'xuv')


except Exception as err:
    print('ERROR OCCURED,PRINTING THE ERROR MESSAGE BELOW:-')
    print(err,file=f)
    f.write(traceback.format_exc())
    f.close()
    print ('TRACEBACK INFO IS WRITTEN TO LOGFILE',logfile)

