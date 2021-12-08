i = int(input())
people = list(map(int, input().split()))
a = [people.index(one) + 1 for one in range(1, i+1)]
print(' '.join(map(str, a)))