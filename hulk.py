s = ''
for i in range(1, int(input())+1):
    if i % 2 == 0:
        s += 'I love that '
    else:
        s += 'I hate that '
print(s[:-5] + 'it')