from basic_players import Player
import random

# Implemente neste arquivo seus jogadores

# Jogador que não faz nada. Subsitua esta classe pela(s) sua(s), ela(s) deve(m) herdar da classe Player

class Weights():

    def __init__(self) -> None:
        self._store=None

    @property
    def store(self):
        return self._store
    @store.setter
    def store(self, store):
        self._store=store

    def gen(self):
        weights=dict()
        for i in range(10):
            for j in range(i, 10):
                weights[(i,j,j+i)]=0
        self.store = weights
        #print(self._store)

    def ajuda_dupla(self,jogadas,tiles,allynot):
        if len(jogadas)>=3:
            p_ally=jogadas[-2]
            if p_ally[3]==None:
                allynot.append(p_ally[1])
                for i in tiles:
                    if i[0] in p_ally[1] or i[1]==p_ally[1]:
                        self.store[(i[0],i[1],i[0]+i[1])]+=1
                        

    def forca_dupla(self, doubles,extremos):
        playable=[]
        pesos=[]
        maior_soma=None
        if len(doubles)!=0:
            for i in doubles:
                if i[0] in extremos or i[1] in extremos:
                    playable.append(i)
                    pesos.append(self._store[i])
            if len(playable)==0:
                return maior_soma
            
            melhor=max(pesos)
            melhor_melhor=-1
            if pesos.count(melhor)>1:
                for i in range(pesos.count(melhor)):
                    if playable[pesos.index(melhor)][2]>melhor_melhor:
                        melhor_melhor=playable[pesos.index(melhor)][2]
                        maior_soma=(playable[pesos.index(melhor)][0],playable[pesos.index(melhor)][1])
                        pesos[pesos.index(melhor)]-=1
                return maior_soma
            else:
                return (playable[pesos.index(melhor)][0],playable[pesos.index(melhor)][1])
        return maior_soma

         

class NonePLayer(Player):
    def __init__(self):
        super().__init__(0, "ASdasd")
        pesos=Weights()
        pesos.gen()
        self._weights = pesos
        self._doubles = None
        self._allynot = []

    def get_doubles(self):
        doubles = []
        for tile in self.tiles:
            if tile[0] == tile[1]:
                doubles.append((tile[0],tile[1],tile[0]+tile[1]))
        self._doubles=doubles

    def play(self, board_extremes, play_hist):


        #print(play_hist)
        playable_tiles = self._tiles
        return 1, random.choice(playable_tiles)
    

    

class Vazio(Player):

    def __init__(self):
        super().__init__(0, "Ninguém")

    def play(self, board_extremes, play_hist):
        return 1, None


# Função que define o nome da dupla:
def pair_name():
    return "algum nome" # Defina aqui o nome da sua dupla

# Função que cria a dupla:
def create_pair():
    return (NonePLayer(), Vazio()) # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.	
