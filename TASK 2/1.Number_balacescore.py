n = input("Enter the n :")   
length = len(n)
half = length // 2
sum1 = 0
sum2 = 0
for i in range(half):
    sum1 = sum1 + int(n[i])
    sum2 = sum2 + int(n[half+i])
if sum1 == sum2:
    print("BALANCED")
else:
    print("NOT BALANCED")
