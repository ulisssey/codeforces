n = int(input())
res = []
count = 0
for i in range(n):
    count = 0
    a, b = map(int, input().split())
    if a % b == 0:
        res.append(count)
    else:
        res.append(b - a % b)
for i in res:
    print(i)