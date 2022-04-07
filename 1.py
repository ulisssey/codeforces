n, k = map(int, input().split())
if (n % k) > 0:
    print(n // k + 1)
else:
    print(int(n / k))