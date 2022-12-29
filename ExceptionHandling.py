num1=int(input('enter a number:'))
num2=int(input('enter s number:'))
try:
    res=num1/num2    #Execute with num2=non zero and zero
except ZeroDivisionError:
    print('Division by zero not allowed')
else:
    print(num1,'/',num2,'=',res)
print("sunil reddy")
