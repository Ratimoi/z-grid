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