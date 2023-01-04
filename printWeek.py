def printWeek(dn):
    wk=''
    if(dn==1):
        wk='sunday'
    elif(dn==2):
        wk='monday'
    elif(dn==3):
        wk= 'tuesday'
    elif(dn==4):
        wk= 'wednesday'
    elif(dn==5):
        wk= 'thursday'
    elif(dn==6):
        wk= 'friday'
    elif(dn==7):
        wk= 'saturday'
    else:
        return 'invalid'
    return wk
import time
for i in range(3):
    inpNum=int(input())
    print(printWeek(inpNum))
