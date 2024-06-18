from basic_players import Player


# Implemente neste arquivo seus jogadores

# Jogador que não faz nada. Subsitua esta classe pela(s) sua(s), ela(s) deve(m) herdar da classe Player

class Weights():
    """
    Decidimos em nosso projeto adicionar um valor numérico a cada peça de \n
    dominó em nosa mão para depois -na função general e sabotage- para isso,\n
    criamos uma classe Weights em que cada jogador terá seu próprio objeto\n
    dessa classe e dentro da classe também estão as funções utilizadas para\n
    aumentar tal valor numérico.
    """
    def __init__(self, hand) -> None:
        self._store = self.gen(hand)

    @property
    def store(self):
        return self._store

    @store.setter
    def store(self, store):
        self._store = store

    def gen(self, hand):
        store = dict()
        for h in hand:
            store[(h[0], h[1], h[0]+h[1])] = 0
        return store

    def propria_mao(self, tiles):
        """
        Valorizamos no dicionário 'mao' cada peça de dominó que temos em \n
        nossa mão, adicionando 1 ponto. \n
        Em seguida, somamos os valores neste dicionário ao dicionário 'store' que contém os pesos de cada \n
        peça de dominó que temos em nossa mão.
        """
        mao = dict()
        for i in tiles:
            if i[0] not in mao.keys():
                mao[i[0]] = 1
            else:
                mao[i[0]] += 1
            if i[1] not in mao.keys():
                mao[i[1]] = 1
            else:
                mao[i[1]] += 1

        for i in tiles:
            if i[0] in mao.keys():
                self.store[(i[0],i[1],i[0]+i[1])]+=mao[i[0]]
            if i[1] in mao.keys():
                self.store[(i[0],i[1],i[0]+i[1])]+=mao[i[1]]

    def ajuda_dupla(self,jogadas,tiles):
        """
        Adicionamos ao dicionário da classe Weights 3 pontos a cada vez que um dominó que temos em nossa \n
        mão tem um número que foi jogado na última jogada de seu aliado, o que depois servirá para \n
        decidir qual peça que será jogada.
        """
        if len(jogadas)>=3:
            p_ally=jogadas[-2]
            for i in tiles:
                if i[0] in p_ally[1] or i[1] in p_ally[1]:
                    self.store[(i[0],i[1],i[0]+i[1])]+=15

    def atrapalha_inimo(self,jogadas,tiles):
        """
        Adicionamos ao dicionário da classe Weights 3 pontos a cada vez que um dominó que temos em nossa \n
        mão não tem um número que foi jogado na última jogada de seu oponente não anterior quando ele não \n
        conseguir jogar uma peça, o que depois servirá para decidir qual peça será jogada.
        """
        if len(jogadas)>=1:
            p_inimigo=jogadas[-1]
            #if p_inimigo[3]==None:
            for i in tiles:
                if i[0] not in p_inimigo[1] or i[1] not in p_inimigo[1]:
                    self.store[(i[0],i[1],i[0]+i[1])]+=15

    def sabotage(self,jogadas,ferradas, extremos, mao):
        """
        Função que decide qual peça será jogada para atrapalhar o inimigo. Verifica-se primeiro se \n
        a antepenúltima jogada, a do inimigo, foi None, ou seja, o inimigo considerou essa peça \n
        desvantajosa para ele. \n
        Caso sim, adicionamos os números dessa peça à lista de peças ferradas e verificamos se temos \n
        alguma peça que possa ser jogada em cima dessa peça. Caso sim, adicionamos as possibilidades \n
        a uma lista e escolhemos a peça com maior peso para ser jogada.
        """
        if len(jogadas)>=3:
            if jogadas[-3][3] is None:
                extremo=jogadas[-3][1]
                ferradas.append(extremo[0])
                ferradas.append(extremo[1])
                possibilidade = []
                for i in mao:
                    if i[0] == extremos[0]:
                        if i[1] in ferradas:
                            possibilidade.append((i[0], i[1], 0))
                    else:
                        if i[1] == extremos[0]:
                            if i[0] in ferradas:
                                possibilidade.append((i[0], i[1], 0))

                    if i[0] == extremos[1]:
                        if i[1] in ferradas:
                            possibilidade.append((i[0], i[1], 1))
                    else:
                        if i[1] == extremos[1]:
                            if i[0] in ferradas:
                                possibilidade.append((i[0], i[1], 1))
                if len(possibilidade) == 0:
                    return None
                maior_peso =- 1
                melhor=possibilidade[0]
                for i in possibilidade:
                    if self.store[i[0],i[1],i[0]+i[1]]>maior_peso:
                        melhor= possibilidade[possibilidade.index(i)]
                return melhor[2],(melhor[0],melhor[1])
            else:
                return None
        else:
            return None


    def general(self, tiles,extremos):
        """
        Função que decide qual peça será jogada. Primeiramente escokhe-se a peça com maior peso e caso haja mais de uma, \n
        escolhe-se a peça que tem a maior soma de seus lados entre as duas peças com maior peso. Caso não haja peças que \n 
        possam ser jogadas, retorna-se None.
        """
        playable=[]
        pesos=[]
        maior_soma=None
        if len(extremos)==0:
            for i in tiles:
                    playable.append(i)
                    pesos.append(self._store[i])

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
            
        if len(tiles)!=0:
            for i in tiles:
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


class Jogador2(Player):

    def __init__(self):
        super().__init__(0, "2")
        pesosdois=Weights(self.tiles)
        self._weights = pesosdois
        self._doublesdois = None
        self._not_doublesdois = None
        self._ferradasdois= []

    def split_tiles(self):
        """
        Separa as peças de dominó em duplas e não-duplas.
        """
        doubles = []
        not_doubles = []
        for tile in self.tiles:
            if tile[0] == tile[1]:
                doubles.append((tile[0],tile[1],tile[0]+tile[1]))
            else:
                not_doubles.append((tile[0],tile[1],tile[0]+tile[1]))
        self._doublesdois=doubles
        self._not_doublesdois = not_doubles

    def play(self, board_extremes, play_hist):
        self.split_tiles()
        #self._weights.ajuda_dupla(play_hist,self._tiles,board_extremes)
        #self._weights.atrapalha_inimo(play_hist,self._tiles)
        if len(self.tiles)==10:
            self._weights.store=self._weights.gen(self.tiles)
        self._weights.propria_mao(self.tiles)
        self._weights.ajuda_dupla(play_hist,self._tiles)
        self._weights.atrapalha_inimo(play_hist,self._tiles)

        if len(board_extremes)==0:
            if len(self._doublesdois)!=0:
                return 1, self._weights.general(self._doublesdois,board_extremes)
            return 1, self._weights.general(self._not_doublesdois,board_extremes)

        if self._weights.sabotage(play_hist,self._ferradasdois,board_extremes,self.tiles)!=None:
            return self._weights.sabotage(play_hist,self._ferradasdois,board_extremes,self.tiles)
        
        if self._weights.general(self._doublesdois,board_extremes)!=None:
            return 1, self._weights.general(self._doublesdois,board_extremes)
        
        return 1, self._weights.general(self._not_doublesdois,board_extremes)

    


class Jogador1(Player):

    def __init__(self):
        super().__init__(0, "1")
        pesos=Weights(self.tiles)
        self._weights = pesos
        self._doubles = None
        self._not_doubles = None
        self._ferradas= []

    def split_tiles(self):
        """
        Separa as peças de dominó em duplas e não-duplas.
        """
        doubles = []
        not_doubles = []
        for tile in self.tiles:
            if tile[0] == tile[1]:
                doubles.append((tile[0],tile[1],tile[0]+tile[1]))
            else:
                not_doubles.append((tile[0],tile[1],tile[0]+tile[1]))
        self._doubles=doubles
        self._not_doubles = not_doubles

    def play(self, board_extremes, play_hist):
        self.split_tiles()

        if len(self.tiles)==10:
            self._weights.store=self._weights.gen(self.tiles)

        self._weights.propria_mao(self.tiles)
        self._weights.ajuda_dupla(play_hist,self._tiles)
        self._weights.atrapalha_inimo(play_hist,self._tiles)
        #self._weights.atrapalha_inimo(play_hist,self._tiles)
        
        if len(board_extremes)==0:
            if len(self._doubles)!=0:
                return 1, self._weights.general(self._doubles,board_extremes)
            return 1, self._weights.general(self._not_doubles,board_extremes)

        if self._weights.sabotage(play_hist,self._ferradas,board_extremes,self.tiles)!=None:
            return self._weights.sabotage(play_hist,self._ferradas,board_extremes,self.tiles)
        
        if self._weights.general(self._doubles,board_extremes)!=None:
            return 1, self._weights.general(self._doubles,board_extremes)
        
        return 1, self._weights.general(self._not_doubles,board_extremes)


# Função que define o nome da dupla:
def pair_name():
    return "Placeholder" # Defina aqui o nome da sua dupla

# Função que cria a dupla:
def create_pair():
    return (Jogador1(), Jogador2()) # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.	