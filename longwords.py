for i in range(int(input())):
    word = input()
    print(word) if len(word) <= 10 else print(f"{word[0]}{len(word[1:-1])}{word[-1]}")