N = int(input("Enter temp:"))
alert = False
for i in range(N):
    temp = int(input())
    if temp > 45:
        alert = True
        break
if alert:
    print("ALERT")
else:
    print("SAFE")
