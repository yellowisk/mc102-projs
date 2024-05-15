def countMostUsed(dictionary):
    mostUsed = []
    highest = 0
    for char in dictionary.items():
        if char[1] >= highest:
            highest = char[1]
    for char in dictionary.items():
        if char[1] == highest:
            mostUsed.append(char[0])
    mostUsed.sort()
    return ''.join(mostUsed)

def getSingleCharacters(text):
    singleCharacters = {}
    try:
        for letter in text:
            keys = singleCharacters.keys()
            if letter in keys:
                singleCharacters[letter] += 1
            else:
                singleCharacters[letter] = 1
        while ' ' in singleCharacters:
            del singleCharacters[' ']
        return singleCharacters
    except EOFError:
        exit()

cases = int(input())

for i in range(cases):
    line = list(input().lower())
    print(countMostUsed(getSingleCharacters(line)))