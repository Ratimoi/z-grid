import os

def getch():
    import sys
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

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
            if linha < len(mapa) - 1:
                linha += 1
        case 'd':
            if coluna < len(mapa[0]) - 1:
                coluna += 1

    mapa[linha][coluna] = 'P'

    return (linha, coluna)

def criar_mapa():
    mapa = []

    for linha in range(10):
        mapa.append([])
        for coluna in range(10):
            mapa[linha].append(".")

    return mapa

def mostrar_mapa(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            print(mapa[linha][coluna], end=" ")
        print()

def colocar_jogador(mapa):
    linha = len(mapa) // 2
    coluna = len(mapa[0]) // 2

    mapa[linha][coluna] = 'P'

    return (linha, coluna)

def colocar_zumbis(mapa):
    zumbis = [(0,0), (7,8), (8,2)]

    for linha, coluna in zumbis:
        if mapa[linha][coluna] == '.':
            mapa[linha][coluna] = 'Z'

    return zumbis

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

def mostrar_ranking():
    try:
        with open("ranking.txt", "r") as f:
            linhas = f.readlines()
    except:
        print("Ranking não encontrado.")
        return
    
    ranking = []
    for linha in linhas:
        nome, pontos = linha.strip().split(":")
        ranking.append((nome, int(pontos)))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\n==== RANKING ====")
    for nome, pontos in ranking:
        print(f"{nome} - {pontos}")

mapa = criar_mapa()
pos_jogador = colocar_jogador(mapa)
zumbis = colocar_zumbis(mapa)

os.system('clear')

nome = input("Digite seu nome: ")
pontos = 0

while True:
    os.system('clear')

    print(f"Pontos: {pontos}\n")

    mostrar_mapa(mapa)
    print()

    comando = getch().lower()

    if comando not in ['w', 'a', 's', 'd']:
        continue

    pos_jogador = mover_jogador(mapa, pos_jogador, comando)

    if pos_jogador in zumbis:
        zumbis = None
    else:
        zumbis = mover_zumbis(mapa, zumbis, pos_jogador)

    if zumbis is None:
        os.system('clear')

        mostrar_mapa(mapa)
        print("GAME OVER")

        break
    else:
        pontos += 10

with open("ranking.txt", "a") as f:
    f.write(f"{nome}:{pontos}\n")

mostrar_ranking()