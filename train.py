n = int(input())
total = []
k = 0
for i in range(n):
    a, b = map(int, input().split())
    k -= a
    k += b
    total.append(k)
print(max(total))
