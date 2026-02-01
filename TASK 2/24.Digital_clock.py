H = int(input("Enter hours:"))
M = int(input("Enter minutes:"))
X = int(input("Enter min to add"))
M = M + X
H = H + (M // 60)
M = M % 60
H = H % 24
print(H, M)
