str = ["ab", "aab", "aaaab", "abc", "xyzab", "abab", "ba"]
for i in str:
    if(i[-1]=="b" and i[-2]=="a"):
        print(i," - matches")
    else:
        print(i," -  not matches")
    
