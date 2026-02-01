n=int(input("Enter num:"))
a=len(str(n))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
if a==4 and sum>15:
    print("Access granted")
else:
    print("Access denied")