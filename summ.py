nums = list(map(int, input().split('+')))
print(''.join(map(str, nums))) if len(nums) == 1 else print('+'.join(map(str, sorted(nums))))