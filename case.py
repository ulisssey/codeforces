s = input()
count1 = 0
count2 = 0
for i in s:
    if i == i.upper():
        count1 += 1
    else:
        count2 += 1
print(s.upper()) if count1 > count2 else print(s.lower())
