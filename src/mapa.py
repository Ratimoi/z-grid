VERDE = "\033[92m"
VERMELHO = "\033[91m"
CINZA = "\033[90m"
RESET = "\033[0m"

PLAYER = "P"
ZUMBI = "Z"
VAZIO = "·"


def criar_mapa():
    mapa = []

    for linha in range(15):
        mapa.append([])
        for coluna in range(15):
            mapa[linha].append(".")

    return mapa


def mostrar_mapa(mapa):
    largura = len(mapa[0])

    print("+" + "--" * largura + "-+")

    for linha in mapa:
        print("|", end=" ")
        for celula in linha:
            if celula == 'P':
                print(VERDE + PLAYER + RESET, end=" ")
            elif celula == 'Z':
                print(VERMELHO + ZUMBI + RESET, end=" ")
            else:
                print(CINZA + VAZIO + RESET, end=" ")
        print("|")

    print("+" + "--" * largura + "-+")