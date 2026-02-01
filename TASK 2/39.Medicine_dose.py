N = int(input())
K = int(input())
count = 0
hour = 0
while hour <= N:
    count += 1
    hour += K
print(count)
