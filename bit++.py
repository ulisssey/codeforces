n = 0
for i in range(int(input())):
    if '++' in input():
        n += 1
    else:
        n -= 1
print(n)