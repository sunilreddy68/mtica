##temp=[]
##for i in range(1,1001):
##    if '6' in str(i):
##        temp.append(i)
##
##print(temp)
##print(len(temp))
          
temp=[i for i in range(900,1001) if '6' in str(i)]
print(temp)
print(len(temp))
