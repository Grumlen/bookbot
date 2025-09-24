def countWords(text):
    return len(text.split())

def countCharacters(text):
    lowerText = text.lower()
    max = len(text)
    characters = {}
    for i in range(0,max):
        c = lowerText[i]
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sortOn(items):
    return items["num"]

def sortDict(characterCount):
    characterList = []
    for letter in characterCount:
        count = characterCount[letter]
        if letter.isalpha():
            characterList.append({ "char": letter, "num": count })
    characterList.sort(reverse=True, key=sortOn)
    return characterList