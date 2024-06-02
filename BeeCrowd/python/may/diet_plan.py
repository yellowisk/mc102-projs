def findLetter(letter: str, letters: list) -> int:
    e = 0
    d = len(letters)
    while e <= d:
        m = int((e + d)/2)
        if m >= len(letters):
            return -1
        if letters[m] == letter:
            return m
        elif letters[m] < letter:
           e = m + 1
        elif letters[m] > letter:
            d = m - 1
    return -1

def orderLetters(letters: list) -> list:
    for i in range(len(letters)):
        for j in range(i+1,len(letters)):
            if letters[i] > letters[j]:
                letters[i],letters[j] = letters[j],letters[i]
    return letters

def isFollowingDiet(diet: str, meals: list) -> bool:
    dietList = orderLetters(list(diet))

    for meal in meals:
        for i in range(len(meal)):
            result = findLetter(meal[i],dietList)
            if result == -1:
                return 'CHEATER'
            else:
                del dietList[result]
    return ''.join(map(str,orderLetters(dietList)))

cases = int(input())
for i in range(cases):
    meals = []
    diet = ''
    missing = []
    for i in range(3):
        data = input()
        if i == 0:
            diet = data
        else:
            meals.append(data)
    veredict = isFollowingDiet(diet,meals)
    if veredict == 'CHEATER':
        print('CHEATER')
    else:
        print(veredict)

    