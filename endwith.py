word = input("Enter a word: ")

if len(word) < 4:
    print(word)
elif word.endswith("est"):
    print(word)
elif word.endswith("er"):
    print(word + "est")
else:
    print(word + "er")
