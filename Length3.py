string='''practice problems for list com pre hension in python.'''
##ans=[]
##wordsList=string.split(' ')
##for i in wordsList:
##    if len(i)==5:
##        ans.append(i)
##print(*ans)


wordsList=string.split(' ')
ans=[i for i in wordsList if len(i)==3]
    
       
print(*ans)
