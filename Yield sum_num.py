def sum_num(a):
    res=0
    for i in range(a+1):
        res=res+i
        yield('i=',i,'res=',res)
    return res
ob=sum_num(19)
for i in range(18):
    print(next(ob))
