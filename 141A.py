str1 = list(input())
str2 = list(input())
str3 = list(input())
new_str = str1 + str2
new_str.sort()
str3.sort()
print('YES') if new_str == str3 else print('NO')
