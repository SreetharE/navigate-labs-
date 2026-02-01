n=int(input("Enter n:"))
total=0
for i in range(n):
    r=float(input("Enter rainfall:"))
    total += r
average = total / n
print("Average rainfall:", average)