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
nao_venceu = True
ja_existe = True
lista_posicao_resposta = []
lista_sorteadas = []

while jogando:
    #confirindo se as coordenadas sao ineditas ou nao 
    
    display = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(display)

    nao_inedita = True
    ja_existe = True
    while nao_inedita: 
        # VEZ DO JOGADOR
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
        

        if coordenadas in lista_posicao_resposta:
            print(f"A posição linha {pergunta_linha} e coluna {pergunta_coluna} já foi informada anteriormente!")
        else:
            lista_posicao_resposta.append(coordenadas)

            tabuleiro_oponente =  faz_jogada(tabuleiro_oponente, pergunta_linha, pergunta_coluna)
            afundou = afundados(frota_oponente, tabuleiro_oponente)
    
            if afundou == len(frota_oponente):
                print('Parabéns! Você derrubou todos os navios do seu oponente!')
                jogando = False
                nao_venceu = False
            nao_inedita = False

    if nao_venceu == True:
        while ja_existe == True:
            #VEZ DO OPONENTE
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)

            coordenadas = [linha , coluna]
            
            if coordenadas not in lista_sorteadas:
                lista_sorteadas.append(coordenadas)

                tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha, coluna)
                print(f'Seu oponente está atacando na linha {linha} e coluna {coluna}')
                    
                afundou_no_mapa_do_jogador = afundados(frota_jogador, tabuleiro_jogador)
                if afundou_no_mapa_do_jogador == len(frota_jogador):
                    print('Xi! O oponente derrubou toda a sua frota =(')
                    jogando = False
                nao_inedita = False 
                ja_existe = False
        
    