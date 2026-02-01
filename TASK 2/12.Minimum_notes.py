amount = int(input())
notes = [500, 200, 100, 50, 20, 10, 1]
count = 0
for note in notes:
    count += amount // note
    amount = amount % note
print(count)
