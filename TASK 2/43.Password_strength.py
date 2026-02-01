N = int(input("Enter n:"))
temp = N
has_seven = False
digit_count = 0
while temp > 0:
    if temp % 10 == 7:
        has_seven = True
    digit_count += 1
    temp //= 10
if has_seven and digit_count >= 6:
    print("STRONG")
else:
    print("WEAK")
