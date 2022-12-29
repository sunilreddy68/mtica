string='practice problems for list com pre hension in python.'
wordsLst=string.split(' ')

wordsLst=[i.strip('\n')for i in wordsLst]

ans={i:i[::-1] for i in wordsLst}
print(ans)
