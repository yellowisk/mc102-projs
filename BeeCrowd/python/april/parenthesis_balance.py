def parenthesisVerifier(math):
    openers = []
    for el in math:
        if el == '(':
            openers.append(el)
        if el == ')':
            if openers == []:
                return "incorrect"
            openers.pop()
    if openers != []:
        return "incorrect"
    else:
        return "correct"

while True:
    try:
        expression = input()
        print(parenthesisVerifier(expression))
    except EOFError:
        break