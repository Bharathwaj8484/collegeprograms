def let(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    c=0
    for char, count in freq.items():
        if count%2==0:
            c+=1
        print(f"{char}-{count}")
    if c>1:
        print("Ans",1)
    else:
        print("Ans",0)
s="cdcdcdcdeeeef"
let(s)
            
