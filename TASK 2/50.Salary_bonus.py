Y = int(input("Enter years of service:"))
if Y < 2:
    bonus = 0
elif Y <= 5:
    bonus = 5000
elif Y <= 10:
    bonus = 10000
else:
    bonus = 20000

print(bonus)
