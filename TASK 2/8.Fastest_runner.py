n=int(input("Enter num of runners:"))
min_time=int(input("Enter min time:"))
for i in range(1,n+1):
    time=int(input("Enter time:"))
    if time<min_time:
        min_time=time
print("Fastest time:",min_time)