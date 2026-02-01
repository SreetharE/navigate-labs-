n = int(input("Enter num:"))
r = 0
while n > 0:
    r = r * 10 + n % 10
    n //= 10
if r < 2:
    print("NOT PRIME")
else:
    for i in range(2, r):
        if r % i == 0:
            print("NOT PRIME")
            break
    else:
        print("PRIME")
