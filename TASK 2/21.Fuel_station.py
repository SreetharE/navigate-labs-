L = float(input())
P = float(input())
bill = L * P
bill_int = int(bill)
last_digit = bill_int % 10
if last_digit <= 4:
    bill_int = bill_int - last_digit
else:
    bill_int = bill_int + (10 - last_digit)

print(bill_int)
