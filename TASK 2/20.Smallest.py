n = int(input("Enter num:"))
for d in range(10):          
    temp = n
    found = False
    while temp > 0:
        if temp % 10 == d:
            found = True
            break
        temp //= 10
    if not found:
        print(d)
        break
