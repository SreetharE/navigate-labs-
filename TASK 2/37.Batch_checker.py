N = int(input("Enter num:"))
last_digit = N % 10
temp = N
while temp >= 10:
    temp //= 10
first_digit = temp

if first_digit != 0 and last_digit % 2 == 0:
    print("VALID")
else:
    print("INVALID")
