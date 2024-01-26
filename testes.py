
#defina posiçao 
def define_posicoes(dic_info):
    lista_posicao = []


    #acessando o valor 
    linha = dic_info["linha"]
    coluna = dic_info["coluna"]
    orientacao = dic_info["orientacao"]
    tamanho = dic_info["tamanho"]

    if orientacao == "vertical" :
        for i in range(linha, linha+tamanho):
        # nosso i vai ser a linha que vai aumentar , pq a coluna nao vai mudar de posicao
            lista_posicao.append([i,coluna])

    if orientacao == "horizontal":
        for a in range(coluna , coluna+ tamanho):
            #agr nosso a que vai aumentando o numero da coluna conforme o tamanho 
            lista_posicao.append([linha,a ])
    
    return lista_posicao

#preencha frota
def preenche_frota(dic_info, nome , lista_frota):
    new_dic = {}

    posicao = define_posicoes(dic_info)

    new_dic["tipo"] = nome
    new_dic["posicoes"] = posicao

    lista_frota.append(new_dic)

    return lista_frota

#faz jogada 
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"

    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"

    return tabuleiro

#posiciona frota
def  posiciona_frota(lista_frota):
    tabuleiro_n_atualizado = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

    for dic in lista_frota:
        for lista_coordenadas in dic["posicoes"]:
            l = lista_coordenadas[0]
            c = lista_coordenadas[1]
            
            tabuleiro_n_atualizado[l][c] = 1

    tabuleiro = tabuleiro_n_atualizado

    return tabuleiro


#Quantas embarcações afundadas?
def afundados(lista_informacoes, tabuleiro_atual):
    afundou = 0
    x = 0

    for dic in lista_informacoes:
        for coordenadas in dic["posicoes"]:
            l = coordenadas[0]
            c = coordenadas[1]
            if tabuleiro_atual[l][c] =="X":
                x+=1
            else:
                break 
        if x == len(dic["posicoes"]):
            afundou+=1
        x = 0
    return afundou

def posicao_valida(dados_de_posicao, frota):
    
    novas_posicoes = define_posicoes(dados_de_posicao)

    for posicao in novas_posicoes:
        linha, coluna = posicao

        if linha < 0 or linha >= 10 or coluna < 0 or coluna >= 10:
            return False
        for navio in frota:
            for posicao_navio in navio['posicoes']:
                if posicao_navio == posicao:
                    return False
    
    return True

import random

def gerando_frota_automaticamente(tabuleiro_oponente, frota_oponente):
    coordenadas_informadas = []

    while True:
        while True:
            linha = input("qual a linha? ")
            if linha.isnumeric() and '0' <= linha <= '9':
                linha = int(linha)
                if 0 <= linha <= 9:
                    break
            print("Linha inválida!")

        while True:
            coluna = input("qual a coluna? ")
            if coluna.isnumeric() and '0' <= coluna <= '9':
                coluna = int(coluna)
                if 0 <= coluna <= 9:
                    break
            print("Coluna inválida!")

        if (linha, coluna) in coordenadas_informadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
            continue
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
        coordenadas_informadas.append((linha, coluna))

        afundou_todas = afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente)
        if afundou_todas:
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            break

frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogo_iterativo(tabuleiro_oponente, frota_oponente)