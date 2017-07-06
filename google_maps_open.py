import webbrowser,sys,time, pyperclip


if len(sys.argv) > 1:
    address='+'.join(sys.argv[1:])
    print ('address from command line argument is', address)

else:
    address=pyperclip.paste()
    print ('ADDRESS FROM THE CLIPBOARD IS:-',address)

address= 'https://www.google.com/maps/place' + '/'+ address
print ('PLEASE GOOGLE MAP THE FOLLOWING ADDRESS:-',address)
time.sleep(5)
webbrowser.open(address)


