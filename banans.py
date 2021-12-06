k, n, w = map(int, input().split())
count = [i * k for i in range(1, w+1)]
print(0) if sum(count) - n == 0 or sum(count) - n < 0 else print(sum(count) - n)
