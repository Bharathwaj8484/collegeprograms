def poly(num):
    s=-1
    l=len(num)
    sum=0
    f=True
    while f==True and l>=0:
        a=num[l-1]
        for i in range(0,l-1):
            sum+=num[i]
        if a<sum:
            s=a+sum
            f=False
        else:
            sum=0
            l-=1
    return s
n=list(map(int, input("Enter n\n").split()))
n.sort()
q=poly(n)
print(q)
