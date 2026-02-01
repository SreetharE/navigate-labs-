B = int(input("Enter battery percentage:"))
D = int(input("Enter discharge rate per hour:"))

hours = 0

if B < 20:
    print(0)
else:
    while B >= 20:
        B -= D
        hours += 1
    print(hours)
