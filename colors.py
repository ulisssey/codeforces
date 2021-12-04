input()
count = 0
colors = input()
i = 0
while i < len(colors):
    if i != len(colors)-1:
        if colors[i] == colors[i+1]:
            count += 1
    i += 1
print(count)
