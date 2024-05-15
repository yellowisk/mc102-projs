def getPokemonAndPlayerPos(matrix):
    pokemon = []
    player = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                player.append(i)
                player.append(j)
            elif matrix[i][j] == 2:
                pokemon.append(i)
                pokemon.append(j)
    return player, pokemon

def getDistance(player, pokemon):
    return abs(player[0] - pokemon[0]) + abs(player[1] - pokemon[1])

try:
    while True:
        rows, columns = map(int,input().split())
        matrix = []
        if rows <= 0 or columns <= 0:
            exit()
        for n in range(rows):
                matrix.append(list(map(int,input().split())))
        playerPos, pokemonPos = getPokemonAndPlayerPos(matrix)
        print(getDistance(playerPos,pokemonPos))
except EOFError:
    exit()