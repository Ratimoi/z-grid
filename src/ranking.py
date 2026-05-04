import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CAMINHO = os.path.join(BASE_DIR, "data", "ranking.txt")

# cores
AZUL = "\033[94m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
VERDE = "\033[92m"
CINZA = "\033[90m"
RESET = "\033[0m"


def mostrar_ranking():
    try:
        with open(CAMINHO, "r") as f:
            linhas = f.readlines()
    except:
        print(VERMELHO + "Ranking não encontrado." + RESET)
        return
    
    ranking = []
    for linha in linhas:
        nome, pontos = linha.strip().split(":")
        ranking.append((nome, int(pontos)))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\n" + AZUL + "═" * 27 + RESET)
    print(AZUL + "🏆        RANKING        🏆" + RESET)
    print(AZUL + "═" * 27 + RESET)

    for i, (nome, pontos) in enumerate(ranking, start=1):
        if i == 1:
            cor = AMARELO   # ouro
            medalha = "🥇"
        elif i == 2:
            cor = CINZA     # prata
            medalha = "🥈"
        elif i == 3:
            cor = VERDE     # bronze (verde ficou melhor visualmente)
            medalha = "🥉"
        else:
            cor = RESET
            medalha = " "

        print(f"{cor}{medalha} {i:02d}. {nome:<10} {pontos:>5} pts{RESET}")

    print(AZUL + "═" * 27 + RESET)


def salvar_ranking(nome, pontos):
    os.makedirs(os.path.dirname(CAMINHO), exist_ok=True)

    with open(CAMINHO, "a") as f:
        f.write(f"{nome}:{pontos}\n")