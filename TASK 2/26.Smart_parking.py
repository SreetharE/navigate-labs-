H = int(input("Enter hours parked:"))
charge = 0

if H <= 2:
    charge = H * 20
elif H <= 5:
    charge = (2 * 20) + (H - 2) * 15
else:
    charge = (2 * 20) + (3 * 15) + (H - 5) * 10

print(charge)
