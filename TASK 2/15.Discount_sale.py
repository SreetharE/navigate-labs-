n=int(input("Enter number:"))
if n<1000:
    discount=0
elif n>=1000 and n<2999:
    discount=0.1*n
elif n>=3000 and n<4999:
    discount=0.2*n
else:
    discount=0.3*n
final_price=n-discount  
print("Final price after discount:",final_price)