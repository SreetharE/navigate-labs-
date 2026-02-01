W=float(input("Enter weight:"))
P=float(input("Enter price per kg:"))
if W>10:
    total=P*W*0.05
else:
    total=P*W
print("Total grocery bill is:",total)