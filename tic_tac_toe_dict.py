def printboard(move, loc, d):
    print('*' * 100)
    if move != ' ':
        print ('YOUR BOARD AFER THE NEW MOVES:-')
        d[loc] = move
    else:
        print('YOUR BOARD BEFORE U BEGIN THE GAME:-')

    print('*' * 100)
    print (d['TOP-L']+' | '+d['TOP-M']+' | '+d['TOP-R'])
    print('-','+','-','+','-')
    print(d['MID-L'] + ' | ' + d['MID-M'] + ' | ' + d['MID-R'])
    print('-', '+', '-', '+', '-')
    print(d['BOT-L'] + ' | ' + d['BOT-M'] + ' | ' + d['BOT-R'])
    print('*' * 100)

def check_results(d):

    if d['TOP-L']=='X':
        if (d['TOP-M'] == 'X' and d['TOP-R'] == 'X') or (d['MID-L'] == 'X' and d['BOT-L'] == 'X') or  (d['MID-M'] == 'X' and d['BOT-R'] == 'X'):
            return 1
    elif d['TOP-L']=='0':
        if (d['TOP-M'] == '0' and d['TOP-R'] == '0') or (d['MID-L'] == '0' and d['BOT-L'] == '0') or (d['MID-M'] == '0' and d['BOT-R'] == '0'):
            return 1
    elif d['TOP-R']=='X':
        if (d['MID-R'] == 'X' and d['BOT-R'] == 'X') or (d['MID-M'] == 'X' and d['BOT-L'] == 'X'):
            return 1
    elif d['TOP-R']=='0':
        if (d['MID-R'] == '0' and d['BOT-R'] == '0') or (d['MID-M'] == '0' and d['BOT-L'] == '0'):
            return 1
    elif (d['BOT-L']=='0' and d['BOT-M']=='0' and d['BOT-R']=='0') or (d['BOT-L']=='X' and d['BOT-M']=='X' and d['BOT-R']=='X'):
        return 1
    elif (d['MID-L']=='0' and d['MID-M']=='0' and d['MID-R']=='0') or (d['MID-L']=='X' and d['MID-M']=='X' and d['MID-R']=='X'):
        return 1
    elif (d['MID-M']=='0' and d['TOP-M']=='0' and d['BOT-M']=='0') or (d['MID-M']=='X' and d['BOT-M']=='X' and d['TOP-M']=='X'):
        return 1




d1 = {'TOP-L': 'X', 'TOP-M': '0', 'TOP-R': 'X', 'MID-L': 'X', 'MID-M': '0', 'MID-R': 'X', 'BOT-L': '0', 'BOT-M': 'X',
         'BOT-R': 'X'}

d = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ', 'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ', 'BOT-L': ' ', 'BOT-M': ' ',
          'BOT-R': ' '}

movesLeft,played=[],[]

for key in d:
    movesLeft.append(key)
printboard(' ',' ',d)
assert len(d)==9 , 'DICTIONARY SHOULD HAVE 9 VARIABLES.'
cnt,outcome=0,0
while(cnt < 10):
    print ('\n'*4)
    print ('PLEASE ENTER THE LOCATION WHR U WANT TO PLACE UR MOVE:-')
    print ('UR OPTIONS ARE ONE OF THE FOLLOWING:-','\n',movesLeft,':-')
    loc=input()
    print('PLEASE ENTER UR MOVE:-')
    move = input()
    if move != 'EXIT':
        if loc in d.keys() and loc not in played:
            if move=='X' or move == '0':
                cnt+=1
                #print ('GOOD MOVE :)',9-cnt, 'MOVES LEFT')
                printboard(move, loc, d)
                #print (d)
                played.append(loc)
                movesLeft.remove(loc)
                outcome=check_results(d)
                if outcome:
                    print ('***** CONGRATS U WON. GAME OVER ********')
                    break
            else:
                print('PLEASE ENTER A VALID MOVE, TRY AGAIN:-')
        else:
            print ('INVALID LOCATION, TRY AGAIN')
    else:
        break



