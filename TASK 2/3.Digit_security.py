n=int(input("Enter a num:"))
sum=0;
a=n
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
if sum%3==0 and a%2==0:
    print("Valid")
else:
    print("Invalid")
