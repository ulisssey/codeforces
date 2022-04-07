n = input()
l = map(int, list(n))
if sum(l) % 3 != 0 or '0' not in n:
    print('NO')
else:
    print('YES')