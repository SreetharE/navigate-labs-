n=int(input("Enetr num:"))
a=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Digit rotation score:",a+rev)