n = int(input())
count = 2
result = []
while count < n:
    if n % count == 0:
        n /= count
        result.append(count)
    else:
        count += 1
result.append(n)
print(result)