a=list(map(int, input("Enter n: ").split()))
n,m=a[0],a[1]
l1= list(map(int, input().split()))
l2= list(map(int, input().split()))
s=0
ma=min(n,m)
for i in range(0,ma):
    if l1[i]<=l2[i]:
        s+=1
print(s)
        
    
