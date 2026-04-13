from mapa import criar_mapa, mostrar_mapa
from jogador import colocar_jogador, mover_jogador
from zumbi import colocar_zumbi, mover_zumbis
from utils import getch, limpar_tela
from ranking import mostrar_ranking, salvar_ranking

limpar_tela()

mapa = criar_mapa()
pos_jogador = colocar_jogador(mapa)

zumbis = []
novo_zumbi = colocar_zumbi(mapa)
zumbis.append(novo_zumbi)

nome = input("Digite seu nome: ")
pontos = 0

while True:
    limpar_tela()

    print(f"Pontos: {pontos} | Zumbis: {len(zumbis)}\n")

    mostrar_mapa(mapa)
    print()

    print("Use W/A/S/D para mover ou Q para sair.")
    comando = getch().lower()

    if comando == 'q':
        break
    elif comando not in ['w', 'a', 's', 'd']:
        continue

    pos_jogador = mover_jogador(mapa, pos_jogador, comando)

    if pos_jogador in zumbis:
        zumbis = None
    else:
        zumbis = mover_zumbis(mapa, zumbis, pos_jogador)

    if zumbis is None:
        limpar_tela()

        mostrar_mapa(mapa)
        print("GAME OVER")

        break
    else:
        pontos += 10

        if pontos % 50 == 0:
            novo_zumbi = colocar_zumbi(mapa)
            zumbis.append(novo_zumbi)

salvar_ranking(nome, pontos)
mostrar_ranking()