def printSunday():
    print('you chose Sunday!\n')
    return
def printMonday():
    print('you chose Monday!\n')
    
def printTuesday():
    print('you chose Tuesday!\n')
    
def printWednesday():
    print('you chose Wednesday!\n')
def printThursday():
    print('you chose Thursday!\n')
def printFriday():
    print('you chose Friday!\n')
def printSaturday():
    print('you chose Saturday!\n')

def choice():
    print('7:Sunday')
    print('1:Monday')
    print('2:Tuesday')
    print('3:Wednesday')
    print('4:Thursday')
    print('5:Friday')
    print('6:Saturday')
    print('8:Quit')
    return
DaySelect={1:printMonday,2:printTuesday,4:printThursday,3:printWednesday,5:printThursday,6:printFriday,7:printSaturday}
selection=1
while True:
    if selection==8:break
    choice()
    selection=int(input('select a Day option:'))
    if(selection>=0) and (selection<8):
        DaySelect[selection]()
