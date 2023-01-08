def RemoveSpecialChar(s):
    ans=[]
    for i in s:
        if i in '1234567890QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfghjklmnbvcxz':
            ans.append(i)
        return ''.join(ans)
inp=input()
print(RemoveSpecialChar(inp))
