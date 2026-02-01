D = int(input("Enter distance:"))
if D <= 5:
    fare = D * 10
elif D <= 15:
    fare = D * 8
else:
    fare = D * 6

print(fare)
