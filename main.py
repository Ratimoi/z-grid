def mover_jogador(mapa, pos, comando):
    linha, coluna = pos
    mapa[linha][coluna] = '.'

    match comando:
        case 'w':
            if linha > 0:
                linha -= 1
        case 'a':
            if coluna > 0:
                coluna -= 1
        case 's':
            if linha < len(mapa):
                linha += 1
        case 'd':
            if coluna < len(mapa[0]):
                coluna += 1
def criar_mapa():
    mapa = []

    for linha in range(10):
        mapa.append([])
        for coluna in range(10):
            mapa[linha].append(".")

    return mapa

def mostar_mapa(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            print(mapa[linha][coluna], end=" ")
        print()
    
    return mapa

def colocar_jogador(mapa):
    linha = len(mapa) // 2
    coluna = len(mapa[0]) // 2

    mapa[linha][coluna] = 'P'

    return (linha, coluna)

def colocar_zumbis(mapa):
    zumbis = [(0,0), (7,8), (8,2)]

    for linha, coluna in zumbis:
        if mapa[linha][coluna] == '.':
            mapa[linha][coluna] == 'Z'

    return zumbis

def mover_zumbi(mapa, pos_zumbi, pos_jogador):
    z_linha, z_coluna = pos_zumbi
    p_linha, p_coluna = pos_jogador

    mapa[z_linha][z_coluna] = '.'

    if z_linha > p_linha:
        z_linha -= 1
    elif z_linha < p_linha:
        z_linha += 1

    if z_coluna > p_coluna:
        z_coluna -= 1
    elif z_coluna < p_coluna:
        z_coluna += 1

    if (z_linha, z_coluna) == 'Z':
        return None
    
    if (z_linha, z_coluna) == pos_jogador:
        return None
    
    mapa[z_linha][z_coluna] == 'Z'

    return (z_linha, z_coluna)

def mover_zumbis(mapa, zumbis, pos_jogador):
    novos_zumbis = []

    for z_pos in zumbis:
        nova_pos = mover_zumbi(mapa, z_pos, pos_jogador)

        if nova_pos is None:
            return None
        
        novos_zumbis.append(nova_pos)

    return novos_zumbis