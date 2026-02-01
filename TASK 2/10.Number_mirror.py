n=int(input("Enter n:"))
a=n
mirror=0
while n>0:
    digit=n%10
    mirror=mirror*10+digit
    n=n//10
if a==mirror:
    print("Number is a mirror number")
else:
    print("Number is not a mirror number")
