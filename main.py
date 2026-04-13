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

    mapa[linha][coluna] = 'P'

    return (linha, coluna)