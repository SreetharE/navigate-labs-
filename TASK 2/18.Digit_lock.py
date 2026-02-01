n = int(input("Enter num:"))
temp = n
has_zero = False
while temp > 0:
    if temp % 10 == 0:
        has_zero = True
        break
    temp //= 10
ends_with_5 = (n % 10 == 5)
if has_zero and ends_with_5:
    print("OPEN")
else:
    print("LOCKED")
