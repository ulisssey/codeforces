k = 2
l = 3
m = 4
n = 5
d = 24
count = 0
for i in range(1, d+1):
    if i % k != 0 and i % l != 0 and i % m != 0 and i % n != 0:
        count += 1
print(d - count)