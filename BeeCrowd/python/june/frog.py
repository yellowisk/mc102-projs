height, amount = map(int, input().strip().split())
pipes = list(map(int, input().split()))

def assess_jump(height: int, current_pipe: int, next_pipe: int) -> bool:
    if height < abs(next_pipe - current_pipe):
        return False
    else:
        return True


def assess_game(height: int, amount: int, pipes: list) -> str:
    if len(pipes) == 1:
        print('YOU WIN')
    
    if len(pipes) == 2:
        if assess_jump(height, pipes[0], pipes[1]):
            print('YOU WIN')
        else:
            print('GAME OVER')
    else:
        if assess_jump(height, pipes[-1], pipes[-2]) == False:
            print('GAME OVER')
            exit() 
        else:
            amount -= 1
            assess_game(height, amount, pipes[:amount])


assess_game(height, amount, pipes)