correct_pin = int(input("Enter correct PIN:"))
access = False
for i in range(3):
    try:
        attempt = int(input())
    except:
        break
    if attempt == correct_pin:
        access = True
        break
if access:
    print("ACCESS GRANTED")
else:
    print("CARD BLOCKED")
