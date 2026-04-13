def mostrar_ranking():
    try:
        with open("data/ranking.txt", "r") as f:
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
    with open("data/ranking.txt", "a") as f:
        f.write(f"{nome}:{pontos}\n")