N = int(input("Enter num:"))
K = int(input("Enter step size:"))
steps = N // K
if N % K != 0:
    steps += 1
print(steps)
