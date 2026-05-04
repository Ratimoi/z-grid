import random

def colocar_zumbi(mapa, pos_jogador):
    while True:
        linha = random.randint(0, len(mapa) - 1)
        coluna = random.randint(0, len(mapa[0]) - 1)

        if mapa[linha][coluna] == '.':
            mapa[linha][coluna] = 'Z'
            return (linha, coluna)

def mover_zumbi(mapa, pos_zumbi, pos_jogador):
    z_linha, z_coluna = pos_zumbi
    p_linha, p_coluna = pos_jogador

    if random.random() < 0.5:
        if z_linha > p_linha:
            z_linha -= 1
        elif z_linha < p_linha:
            z_linha += 1
    else:
        if z_coluna > p_coluna:
            z_coluna -= 1
        elif z_coluna < p_coluna:
            z_coluna += 1

    z_linha = max(0, min(z_linha, len(mapa) - 1))
    z_coluna = max(0, min(z_coluna, len(mapa[0]) - 1))

    if (z_linha, z_coluna) == pos_jogador:
        return None

    return (z_linha, z_coluna)

def mover_zumbis(mapa, zumbis, pos_jogador):
    for linha, coluna in zumbis:
        mapa[linha][coluna] = '.'

    novos_zumbis = []

    for z_pos in zumbis:
        nova_pos = mover_zumbi(mapa, z_pos, pos_jogador)

        if nova_pos is None:
            return None
        if nova_pos not in novos_zumbis:
            novos_zumbis.append(nova_pos)

    for linha, coluna in novos_zumbis:
        mapa[linha][coluna] = 'Z'

    return novos_zumbis