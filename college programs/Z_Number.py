def znum(st):
    n=len(st)
    ic=True
    dc=True
    for i in range(n-1):
        if i%2==0:
            if st[i] <= st[i+1]:
                ic=False
            if st[i] >= st[i+1]:
                dc=False
        else:
            if st[i] >= st[i+1]:
                ic=False
            if st[i] <= st[i+1]:
                dc=False
    return ic or dc 
n=15
c=0
zz=[]
for i in range(0,n+1):
    if znum(str(i)):
        c+=1
        zz.append(i)
print(c)
print(zz)
