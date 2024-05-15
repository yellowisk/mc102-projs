h1, m1, h2, m2 = map(int, input().split())

while True:
    if h1 == m1 == h2 == m2 == 0:
        break
    
    if h1 == h2:
        if m1 == m2:
            print(0)
        elif m1 < m2:
            print(m2 - m1)
        else:
            print(24*60-(m1-m2))
    elif h1 < h2:
        hours = h2 - h1
        if m1 == m2:
            print(hours * 60)
        elif m1 < m2:
            print(hours * 60 + m2 - m1)
        else:
            print((hours - 1) * 60 + (60 - m1) + m2)
    else:
        hours = 24 - (h1 - h2)
        if m1 == m2:
            print((hours) * 60)
        elif m1 <= m2:
            print((hours) * 60 + m2 - m1)
        else:
            print((hours - 1) * 60 + (60 - m1) + m2)
    h1, m1, h2, m2 = map(int, input().split())