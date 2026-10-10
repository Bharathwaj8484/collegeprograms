a=[1,2,3]
b=[2,3]
c=[2]
X = list(set(a) - set(b))[0]
Y = list(set(b) - set(c))[0]
print(X)
print(Y)
