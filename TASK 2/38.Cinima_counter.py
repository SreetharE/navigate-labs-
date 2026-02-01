S = int(input("Enter seats available:"))
N = int(input("Enter number of bookings:"))
for i in range(N):
    if S > 0:
        print("BOOKED")
        S=S-1
    else:
        print("HOUSEFULL")
        break
else:
    print(S)
