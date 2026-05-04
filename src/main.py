from mapa import criar_mapa, mostrar_mapa
from jogador import colocar_jogador, mover_jogador
from zumbi import colocar_zumbi, mover_zumbis
from utils import getch, limpar_tela
from ranking import mostrar_ranking, salvar_ranking

limpar_tela()

mapa = criar_mapa()
pos_jogador = colocar_jogador(mapa)

zumbis = []
zumbis.append(colocar_zumbi(mapa, pos_jogador))

nome = input("Digite seu nome: ")
pontos = 0

dificuldade = 1
ultimo_spawn = 0

while True:
    limpar_tela()

    print(f"Pontos: {pontos} | Zumbis: {len(zumbis)} | Dificuldade: {dificuldade}\n")

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

    pontos += 10

    if pontos >= 300:
        dificuldade = 3
    elif pontos >= 100:
        dificuldade = 2
    else:
        dificuldade = 1

    if dificuldade == 1:
        spawn_rate = 50
        max_zumbis = 3
    elif dificuldade == 2:
        spawn_rate = 30
        max_zumbis = 6
    else:
        spawn_rate = 15
        max_zumbis = 10

    if pontos - ultimo_spawn >= spawn_rate and len(zumbis) < max_zumbis:
        novo_zumbi = colocar_zumbi(mapa, pos_jogador)
        zumbis.append(novo_zumbi)
        ultimo_spawn = pontos

salvar_ranking(nome, pontos)
mostrar_ranking()