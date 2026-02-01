D=int(input("Enter days:"))
if 1<=D<=5:
    fee=D*2
    print("Late fee is:",fee)
elif 6<=D<=10:
    fee=D*3
    print("Late fee is:",fee)
elif D>10:
    fee=D*5
    print("Late fee is:",fee)   