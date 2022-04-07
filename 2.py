x1, x2, x3 = map(int, input().split())
count = 0
y1 = 0
if x1 > x2:
    count += (x1 - x2)
    y1 = x2
elif x2 > x1:
    count += (x2 - x1)
    y1 = x2
if y1 > x3:
    count += (y1 - x3)
elif x3 > y1:
    count += (x3 - y1)
print(count + (x3 - x1))