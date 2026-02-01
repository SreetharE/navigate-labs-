b = int(input("Enter balance: "))
w = int(input("Enter withdraw amount: "))

if w % 100 == 0:
    if w <= b:
        b = b - w
        if b >= 500:
            print("SUCCESS")
        else:
            print("Low balance")
    else:
        print("REJECTED")
else:
    print("Withdraw amount must be multiple of 100")
