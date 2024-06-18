def walk(formiga, board, t):
    if t == 0:
        return

    x, y, direction = formiga

    if board[x][y] == '.':
        if direction == 'up':
            direction = 'right'
            board[x][y] = '#'
            y += 1
        elif direction == 'right':
            direction = 'down'
            board[x][y] = '#'
            x += 1
        elif direction == 'down':
            direction = 'left'
            board[x][y] = '#'
            y -= 1
        else:
            direction = 'up'
            board[x][y] = '#'
            x -= 1
    else:
        if direction == 'up':
            direction = 'left'
            board[x][y] = '.'
            y -= 1
        elif direction == 'right':
            direction = 'up'
            board[x][y] = '.'
            x -= 1
        elif direction == 'down':
            direction = 'right'
            board[x][y] = '.'
            y += 1
        else:
            direction = 'down'
            board[x][y] = '.'
            x += 1

    formiga = (x, y, direction)
    walk(formiga, board, t - 1)


def langton(t, m, n, board):
    ant = (m // 2, n // 2, 'down')
    walk(ant, board, t)

    for line in board:
        print("".join(line))

t, m, n = map(int, input().split())
board = [list(input()) for _ in range(m)]

langton(t, m, n, board)
