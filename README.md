# 🧟 Z-Grid

Um jogo feito totalmente em python sobre zumbis que te perseguem dentro de uma matriz, onde o objetivo principal é sobreviver o máximo de tempo que conseguir e alcançar o maior ranking de pontos possível.

---

## 🎮 Como Jogar

* O Jogador (`P`) se locomove pelo mapa através:
  * `W` - Para cima
  * `A` - Para direita
  * `S` - Para baixo
  * `D` - Para esquerda
* Os Zumbis (`Z`) se locomovem automaticamente atrás do jogador
* Cada rodada sobrevivida você recebe +10 pontos
* Caso o Zumbi alcance o jogador é Game Over

---

## 🧱 Estrutura do Projeto

```text
z-grid/
|
├── src/
|   ├── main.py
|   ├── mapa.py
|   ├── jogador.py
|   ├── zumbi.py
|   ├── ranking.py
|   └── utils.py
|
├── data/
|   ├── ranking.txt
|   └── .gitkeep
|
├── .gitignore
├── README.md
└── LICENSE
```
---

## 🚀 Funcionalidades do Projeto

* Movimentação em tempo real (Sem necessidade do Enter)
* Sistema de pontuação
* Ranking salvo em arquivo
* Múltiplos zumbis
* Estrutura modular

---

## ▶️ Como Executar

### 1. Clone o Repositório:
``` bash
git clone https://github.com/Ratimoi/z-grid.git
```

### 2. Execute o jogo:
``` bash
python3 src/main.py
```

---

## 🧠 Tecnologias Utilizadas

* Python 3
* Terminal Linux (uso de termios e tty)

---

## 📈 Versão Atual

v1.0.0 - primeira versão jogável

---

## 🔮 Futuras Atualizações

* Spawn dinâmico
* Sistema de dificuldade
* Menus em terminal
* Sons e músicas
* Obstáculos no mapa
* Itens auxiliares

---

## 👨‍💻 Autor

Projeto desenvolvido por Ramiro Quevedo Paz
