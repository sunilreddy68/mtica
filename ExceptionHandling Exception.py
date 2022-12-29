num1=input('enter a number:')
num2=input('enter a number:')
try:
    res=int(num1)/int(num2)    #Execute with num2=non zero and zero
except ZeroDivisionError:
    print('Exception handled by sunil reddy')
except ValueError:
    print('Exception handled by sunil reddy')
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
    print("sunil reddy")

print("good night")
