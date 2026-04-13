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