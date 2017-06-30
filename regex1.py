import re
expr=r'^[+-]?(\d)*\.(\d)+$'
for i in range(int(input())):
    mo=re.search(expr,input())
    print (bool(mo))
