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