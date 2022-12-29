def Factorial(num):
    assert(isinstance(num,int)),'factorial of negative number is not integer!'
    assert(num>=0),'factorial of negative number is not defined!'
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-45))
except Exception as obj:
        print(obj)
try:
    print(Factorial(45))
except Exception as obj:
    print(obj)
    
try:
    print(Factorial(99.9))
except Exception as obj:
    print(obj)
try:
    print(Factorial('sunil reffy'))
except Exception as obj:
    print(obj)
    
