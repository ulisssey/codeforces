_, h = map(int, input().split())
count = 0
n = map(int, input().split())
for i in n:
    if i > h:
        count += 2
    else:
        count += 1
print(count)