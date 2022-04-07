n = int(input())
count = 0
a = []
b = []
for i in range(n):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            count += 1
print(count)