import random
from funcoes import *

# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True
nao_inedita = True
lista_posicao_resposta = [] 

while jogando:
    #confirindo se as coordenadas sao ineditas ou nao 
    
    display = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(display)

    nao_inedita = True
    while nao_inedita: 
    
        #perguntando a linha
        pergunta_linha = int(input("Em qual linha deseja atacar: ?"))

        while pergunta_linha >= 10 or pergunta_linha < 0 :
            print('Linha inválida!')
            pergunta_linha = int(input("Em qual linha deseja atacar: ?"))
            
        #perguntando a coluna   
        pergunta_coluna = int(input("Em que coluna deseja atacar: ?"))

        while pergunta_coluna >= 10 or pergunta_coluna < 0:
            print('Coluna inválida!')
            pergunta_coluna = int(input("Em que coluna deseja atacar: ?"))
    

        coordenadas =[pergunta_linha,pergunta_coluna]
        
        if coordenadas not in lista_posicao_resposta:
            lista_posicao_resposta.append(coordenadas)
            nao_inedita = False
        else:
            print(f"A posição linha {pergunta_linha} e coluna {pergunta_coluna} já foi informada anteriormente!")

    tabuleiro_oponente =  faz_jogada(tabuleiro_oponente, pergunta_linha, pergunta_coluna)


    afundou = afundados(frota_oponente, tabuleiro_oponente)

    if afundou == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
                
