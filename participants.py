amount, place = map(int, input().split())
scores = list(map(int, input().split()))
number = [i for i in scores if i >= scores[place-1] and i > 0]
print(0) if sum(scores) == 0 else print(len(number))