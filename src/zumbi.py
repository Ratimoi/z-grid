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

    if z_linha > p_linha:
        z_linha -= 1
    elif z_linha < p_linha:
        z_linha += 1

    if z_coluna > p_coluna:
        z_coluna -= 1
    elif z_coluna < p_coluna:
        z_coluna += 1

    z_linha = max(0, min(z_linha, len(mapa) - 1))
    z_coluna = max(0, min(z_coluna, len(mapa[0]) - 1))

    if (z_linha, z_coluna) == pos_jogador:
        return None

    return (z_linha, z_coluna)

def mover_zumbi(mapa, pos_zumbi, pos_jogador):
    z_linha, z_coluna = pos_zumbi
    p_linha, p_coluna = pos_jogador

    delta_linha = p_linha - z_linha
    delta_coluna = p_coluna - z_coluna

    if abs(delta_linha) > abs(delta_coluna):
        if delta_linha > 0:
            z_linha += 1
        elif delta_linha < 0:
            z_linha -= 1
    else:
        if delta_coluna > 0:
            z_coluna += 1
        elif delta_coluna < 0:
            z_coluna -= 1

    if (z_linha, z_coluna) == pos_jogador:
        return None

    return (z_linha, z_coluna)