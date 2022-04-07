n = int(input())
count = n
for i in range(n):
    s = input()
    if '-' in s:
        count -= 1
    elif '+' in s:
        a, b = s.split('+')
        count += int(b)
print(count)