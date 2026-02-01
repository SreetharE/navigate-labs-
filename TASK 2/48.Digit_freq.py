N = int(input("Enter num:"))
D = int(input("Enter digit:"))
temp = N
count = 0
while temp > 0:
    if temp % 10 == D:
        count += 1
    temp //= 10
print(count)
