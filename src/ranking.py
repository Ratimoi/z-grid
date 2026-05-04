import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CAMINHO = os.path.join(BASE_DIR, "data", "ranking.txt")


def mostrar_ranking():
    try:
        with open(CAMINHO, "r") as f:
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


def salvar_ranking(nome, pontos):
    os.makedirs(os.path.dirname(CAMINHO), exist_ok=True)

    with open(CAMINHO, "a") as f:
        f.write(f"{nome}:{pontos}\n")