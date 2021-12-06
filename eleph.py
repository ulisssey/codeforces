x = int(input())
count = 0
count += x // 5
if x % 5 == 0:
    print(count)
else:
    count += 1
    print(count)
