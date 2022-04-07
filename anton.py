word = input()[1:-1]
if len(word) < 1:
    print(0)
else:
    words = list(word.split(', '))
    new_words = set(words)
    print(len(new_words))