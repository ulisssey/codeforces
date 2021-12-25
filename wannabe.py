levels = int(input())
p = list(input().split())[1:]
q = list(input().split())[1:]
s = p + q
print('I become the guy.') if len(set(s)) == levels else print('Oh, my keyboard!')