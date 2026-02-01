n=int(input("Enter num:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
if sum%9==0:
    print("Valid ticket")
else:
    print("Invalid ticket")