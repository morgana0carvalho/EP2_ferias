import random
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

#posicao valida
def posicao_valida(dic_info,lista_frota):

    lista_nova_posicoes = define_posicoes(dic_info)

    for posicao in lista_nova_posicoes:
        #linha , coluna = posicao

        linha = posicao[0]
        coluna = posicao[1]

        if linha < 0 or linha >= 10 or coluna < 0 or coluna >= 10:
            return False

        for navio_dic in lista_frota :
            if posicao in navio_dic["posicoes"]:
                return False
                   
    return True       

import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota

