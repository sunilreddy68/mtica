def div(a,b):
    assert (b!=0),"Division by zero is not defined"
    return a/b

try:
    print(div(100,0))
except  AssertionError as obj:
        print(obj)
try:
    print(div(45,23))
except AssertionError as obj:
    print(obj)
    
try:
    print(div(99,45))
except AssertionError as obj:
    print(obj)
