n=int(input("Enter num:"))
sum=0
product=1
while n>0:
    digit=n%10
    sum=sum+digit
    product=product*digit
    n=n//10
if sum%2==0 and product%3==0:
    print("Valid coupon")
else:
    print("Invalid coupon")
