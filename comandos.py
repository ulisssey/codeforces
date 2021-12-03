count = 0
for i in range(int(input())):
    a = input().count('1')
    if a > 1:
        count += 1
print(count)