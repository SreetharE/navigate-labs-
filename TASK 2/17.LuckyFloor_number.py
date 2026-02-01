n = int(input("Enter num:"))
count = 0
for num in range(1, n + 1):
    temp = num
    has_four = False
    while temp > 0:
        if temp % 10 == 4:
            has_four = True
            break
        temp //= 10
    if not has_four:
        count += 1
print(count)
