def uses_only(letter,s):
    word =letter.strip()
    print(word)
    for c in word:
        if c not in s:
            return False
    return True



a=uses_only('hoe alfalfa','acefhlo')
print(a)