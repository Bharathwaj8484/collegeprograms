def st(s):
    fb = False
    for i in s:
        if i=="b":
            fb=True
        if fb and i=="a":
            return False
        if i!="a" and i!="b":
            return False
    return fb and 'a' in s
s = input("Enter strings separated by spaces: ").split()
ss=0
for j in s:
    if st(str(j)):
        ss+=1
print(ss)
