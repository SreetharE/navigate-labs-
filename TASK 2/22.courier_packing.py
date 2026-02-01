L=int(input("Enter length:"))
W=int(input("Enter width:"))
H=int(input("Enter height:"))
if L>0 and W>0 and H>0 and L+W+H<=150:
    print("Accepted")
else:
    print("Rejected")