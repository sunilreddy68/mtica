spins=[('red','18'),('black','13'),('red','7'),('red','35'),('black','23'),('red','8'),('black','45'),('red','98'),('back','7')]
def countReds(aList):
    count=0
    for color,number in aList:
        if color=='black':
            yield count
            count=0
        else:
            count+=1
        yield count
gaps=[gap for gap in countReds(spins)]
print(gaps)
       
