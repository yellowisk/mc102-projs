def atLeastOneAttended(alumni, dinners):
    if alumni == 0 or dinners == 0:
        return

    for h in range(alumni):
        general.append(0)

    for i in range(dinners):
        j = 0
        atendance = list(map(int, input().split()))
        for k in atendance:
            if k == 1:
                general[j] += 1
            j += 1

    if dinners in general:
        print('yes')
    else:
        print('no')

while True:
    try:
        alumni, dinners = map(int, input().split())
        general = []
        atLeastOneAttended(alumni, dinners)
    except EOFError:
        break
