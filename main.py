def criar_mapa():
    mapa = []

    for linha in range(10):
        mapa.append([])
        for coluna in range(10):
            mapa[linha].append(".")

    return mapa