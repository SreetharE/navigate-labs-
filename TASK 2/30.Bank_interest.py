B = int(input("Enter bank balance:"))
if B < 10000:
    rate = 0.03
elif B <= 50000:
    rate = 0.05
else:
    rate = 0.07
monthly_interest = (B * rate) / 12
print(monthly_interest)
