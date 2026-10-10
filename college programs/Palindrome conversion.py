n = 195
while True:
    r = int(str(n)[::-1])
    if n==r:
        print("Reversed Number:", n)
        break
    else:
        n+=r
