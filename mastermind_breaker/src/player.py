#!/usr/bin/env python3
"""
Implemente aqui o seu código para o jogador.

Seu principal objetivo é implementar a função `player`, que deve retornar uma lista de 4 cores, o seu próximo palpite.
Como exemplo, a função abaixo retorna um palpite aleatório.

Dicas:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
"""
from random import randrange, choice
from colors import *

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
c_dict =  {
    1: RED, 2: GREEN,3: BLUE,
    4: YELLOW, 5: ORANGE, 6: BLACK,
    7: WHITE
}

#Cria lista com todas as possibilidades de chute
saved = []
for i in range(1,8):
    for j in range(1,8):
        for k in range(1,8):
            for l in range(1,8):
                if i!=j!=k!=l and j!=i!=k!=l and k!=j!=i!=l and l!=j!=k!=i:
                    saved.append([i,j,k,l])


def convert_color_to_int(guess):
    '''Transforma as cores de um chute para int'''
    block = []
    for el in guess:
        for color in c_dict.items():
            if color[1].__str__() == el.__str__():
                block.append(color[0])
    num_guess_hist.append(block)
    return num_guess_hist


def convert_int_to_color(guess):
    '''Transforma os ints de um chute para color'''
    block = []
    for k in range(len(guess)):
        for cor in c_dict.items():
            if cor[0] == guess[k]:
                block.append(cor[1])
    return block


def del_general(num_guess_hist, res_hist):
    '''Deletes all lists that contain the guess' numbers, regardless of any order'''
    guess = num_guess_hist[-1]
    if res_hist[-1][0] != 4:
        copia = possibilities.copy()
        for i in copia:
            if guess[0] in i and guess[1] in i and guess[2] in i and guess[3] in i:
                lista_pesos.remove(lista_pesos[possibilities.index(i)])
                possibilities.remove(i)


def del_if_four(num_guess_hist, res_hist):
    '''Se as quatro cores de um chute estiverem corretas, remove todos que não 
    têm todas estas cores'''
    guess = num_guess_hist[-1]
    copia = possibilities.copy()
    if res_hist[-1][0]==4:
        for i in copia:
            if guess[0] not in i or guess[1] not in i or guess[2] not in i  or guess[3] not in i:
                lista_pesos.remove(lista_pesos[possibilities.index(i)])
                possibilities.remove(i)


def del_if_zero(num_guess_hist, res_hist):
    '''Se nenhuma cor de um chute estiver na posição correta, remove todos os chutes 
    que têm alguma dessas cores na mesma posição do chute'''
    guess = num_guess_hist[-1]
    copia = possibilities.copy()
    if res_hist[-1][1] == 0:
        for i in copia:
            if i[0] == guess[0] or i[1] == guess[1] or i[2] == guess[2] or i[3] == guess[3]:
                lista_pesos.remove(lista_pesos[possibilities.index(i)])
                possibilities.remove(i)

#Remove o último chute dado se ele estiver incorreto
def del_last_guess(num_guess_hist):
    global possibilities
    try:
        lista_pesos.remove(lista_pesos[possibilities.index(num_guess_hist[-1])])
        possibilities.remove(num_guess_hist[-1])
    except ValueError:
        pass


def del_certeza_pos(num_guess_hist, res_hist):
    '''Remove todos os chutes que tem um número diferente de cores na mesma posição do último chute, 
    caso eles tenham o mesmo número de cores na posição correta'''
    global possibilities
    global lista_pesos
    copia = possibilities.copy()
    guess = num_guess_hist[-1]
    if res_hist[-1][1] != 0:
        for i in copia:
            cont = 0
            if i[0] == guess[0]:
                cont += 1
            if i[1] == guess[1]:
                cont += 1
            if i[2] == guess[2]:
                cont += 1
            if i[3] == guess[3]:
                cont += 1
            if cont != res_hist[-1][1]:
                del lista_pesos[possibilities.index(i)]
                possibilities.remove(i)


def add_peso_pos(num_guess_hist, res_hist):
    '''Valorizamos mais todos os chutes que tem elementos na mesma posição do último chute dado, 
    caso eles tenham o mesmo número de cores na posição correta'''
    global possibilities
    global lista_pesos
    copia = possibilities.copy()
    guess = num_guess_hist[-1]
    if res_hist[-1][1] != 0:
        for i in copia:
            cont = 0
            if i[0] == guess[0]:
                cont += 1
            if i[1] == guess[1]:
                cont += 1
            if i[2] == guess[2]:
                cont += 1
            if i[3] == guess[3]:
                cont += 1
            if cont == res_hist[-1][1]:
                lista_pesos[possibilities.index(i)] += 1


def del_certeza_ex(num_guess_hist, res_hist):
    '''Remove todos os chutes que tem um número diferente de cores em qualquer posição 
    do último chute, caso eles tenham o mesmo número de cores corretas'''
    global maximo
    guess = num_guess_hist[-1]
    global possibilities
    global lista_pesos
    copia=possibilities.copy()
    for i in copia:
        cont = 0
        if i[0] in guess:
            cont += 1
        if i[1] in guess:
            cont += 1
        if i[2] in guess:
            cont += 1
        if i[3] in guess:
            cont += 1
        if cont != res_hist[-1][0]:
            del lista_pesos[possibilities.index(i)]
            possibilities.remove(i)

def add_peso_ex(num_guess_hist,res_hist):
    '''Valorizamos mais todos os chutes que tem os mesmos elementos do último chute dado, 
    caso eles tenham o mesmo número de cores corretas'''
    global maximo
    guess = num_guess_hist[-1]
    global possibilities
    global lista_pesos
    copia = possibilities.copy()
    for i in copia:
        cont=0
        if i[0] in guess:
            cont += 1
        if i[1] in guess:
            cont += 1
        if i[2] in guess:
            cont += 1
        if i[3] in guess:
            cont += 1
        if cont == res_hist[-1][0]:
            lista_pesos[possibilities.index(i)] += 1


def todos_casos(saved: list):
    '''Caso a lista de chutes não exista é atribuída a ela todos os chutes possíveis'''
    global possibilities
    try:
        possibilities[0]
    except:
        possibilities = saved.copy()


def get_random(pesos: list, possibilities: list):
    '''Dentre os chutes com maior peso, escolhemos um deles aleatoriamente'''
    higher = max(pesos)
    next_guess = None
    if pesos.count(higher) > 1:
        index = randrange(len(pesos))
        next_guess = possibilities[index]
        return next_guess
    else:
        return possibilities[pesos.index(higher)]


def get_random_without_weights(possibilities):
    '''Dentre os chutes disponíveis, escolhemos um deles aleatoriamente'''
    return choice(possibilities)


def reset():
    '''Reseta as variáveis para cada jogo novo'''
    global possibilities
    global lista_pesos
    global num_guess_hist
    num_guess_hist = []
    possibilities = []
    lista_pesos = [0]*840


def removal_spree(num_guess_hist, res_hist):
    '''Junção das funções dos casos gerais'''
    del_last_guess(num_guess_hist)
    del_general(num_guess_hist,res_hist)
    del_if_zero(num_guess_hist,res_hist)
    del_if_four(num_guess_hist,res_hist)
    del_certeza_pos(num_guess_hist,res_hist)
    del_certeza_ex(num_guess_hist,res_hist)

def player(guess_hist, res_hist):
    if guess_hist == []:
        reset()
        todos_casos(saved)
        return convert_int_to_color([1,2,3,4])
    if len(guess_hist)==1:
        if res_hist[-1][0] == 1:
            convert_int_to_color(guess_hist[-1])
            removal_spree(num_guess_hist, res_hist)
            return convert_int_to_color([1,5,6,7])
        else:
            convert_color_to_int(guess_hist[-1])
            removal_spree(num_guess_hist, res_hist)
            return convert_int_to_color(get_random_without_weights(possibilities))
    else:
        convert_color_to_int(guess_hist[-1])
        removal_spree(num_guess_hist, res_hist)
        return convert_int_to_color(get_random_without_weights(possibilities))
