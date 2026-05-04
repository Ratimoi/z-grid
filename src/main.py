import time

from mapa import criar_mapa, mostrar_mapa
from jogador import colocar_jogador, mover_jogador
from zumbi import colocar_zumbi, mover_zumbis
from utils import getch, limpar_tela
from ranking import mostrar_ranking, salvar_ranking


def calcular_dificuldade(pontos):
    if pontos >= 300:
        return 3
    elif pontos >= 100:
        return 2
    return 1


def parametros_dificuldade(dificuldade):
    if dificuldade == 1:
        return 50, 3, 0.5
    elif dificuldade == 2:
        return 30, 6, 0.3
    return 15, 10, 0.15


def deve_spawnar(pontos, ultimo_spawn, spawn_rate, zumbis, max_zumbis):
    return (
        pontos - ultimo_spawn >= spawn_rate
        and len(zumbis) < max_zumbis
    )


limpar_tela()

mapa = criar_mapa()
pos_jogador = colocar_jogador(mapa)

zumbis = [colocar_zumbi(mapa, pos_jogador)]

nome = input("Digite seu nome: ")
pontos = 0

ultimo_spawn = 0
ultimo_mov_zumbi = time.time()


while True:
    limpar_tela()

    dificuldade = calcular_dificuldade(pontos)
    spawn_rate, max_zumbis, intervalo_zumbi = parametros_dificuldade(dificuldade)

    print(f"Pontos: {pontos} | Zumbis: {len(zumbis)} | Dificuldade: {dificuldade}\n")
    mostrar_mapa(mapa)
    print()
    print("Use W/A/S/D para mover ou Q para sair.")

    comando = getch().lower()

    if comando == 'q':
        break
    elif comando in ['w', 'a', 's', 'd']:
        pos_jogador = mover_jogador(mapa, pos_jogador, comando)

    agora = time.time()
    if agora - ultimo_mov_zumbi >= intervalo_zumbi:
        if pos_jogador in zumbis:
            zumbis = None
        else:
            zumbis = mover_zumbis(mapa, zumbis, pos_jogador)

        ultimo_mov_zumbi = agora

    if zumbis is None:
        limpar_tela()
        mostrar_mapa(mapa)
        print("GAME OVER")
        break

    pontos += 10

    if deve_spawnar(pontos, ultimo_spawn, spawn_rate, zumbis, max_zumbis):
        novo_zumbi = colocar_zumbi(mapa, pos_jogador)
        zumbis.append(novo_zumbi)
        ultimo_spawn = pontos


salvar_ranking(nome, pontos)
mostrar_ranking()