def checkEven(num):
    
    if num%2==0:
        return "even"
        
        
def checkOdd(num):
    if num%2==1:
        return "odd"
num=int(input("Enter a no:"))
x=checkEven(num)
y=checkOdd(num)
print("x=",x)
print("y=",y)

    
print(checkEven(num))
print(checkOdd(num))
