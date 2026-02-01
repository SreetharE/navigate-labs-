n=int(input("Enter Id:"))
a=len(str(n))
if a==6 and n%7==0:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")